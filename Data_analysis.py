import pandas as pd
import numpy as np
from scipy.stats import ttest_rel, levene, pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. DATA LOADING & CLEANING ---
try:
    ign = pd.read_csv('Databases/IGN_data.csv')
    meta = pd.read_csv('Databases/metacritic_pc_games.csv')
    oc = pd.read_csv('Databases/Opencritic_dataset.csv')
except FileNotFoundError:
    ign = pd.read_csv('IGN_data.csv')
    meta = pd.read_csv('metacritic_pc_games.csv')
    oc = pd.read_csv('Opencritic_dataset.csv')

for df in [ign, meta, oc]:
    df.columns = df.columns.str.strip()

# Standardizing Column Names
meta.rename(columns={'Game Title':'game', 'Overall Metascore':'critic_score', 
                     'Overall User Rating':'user_score', 'Game Release Date':'date'}, inplace=True)
oc.rename(columns={'Title':'game', 'Score':'critic_score_oc', 'Release Date':'date_oc'}, inplace=True)
ign.rename(columns={'game':'game', 'score':'critic_score_ign', 'released_date':'date_ign'}, inplace=True)

# Date Conversion
meta['date'] = pd.to_datetime(meta['date'], errors='coerce')
oc['date_oc'] = pd.to_datetime(oc['date_oc'], errors='coerce')
ign['date_ign'] = pd.to_datetime(ign['date_ign'], errors='coerce')

# Merging
merged = meta.merge(oc, on='game', how='outer').merge(ign, on='game', how='outer')

# --- 2. NORMALIZATION (Scaling all to 0-100) ---
for col in ['critic_score', 'user_score', 'critic_score_oc', 'critic_score_ign']:
    merged[col] = pd.to_numeric(merged[col], errors='coerce')

# Scaling 0-10 sources to 0-100
merged['user_score'] = merged['user_score'] * 10
merged['critic_score_ign'] = merged['critic_score_ign'] * 10

# Year consolidation
merged['year'] = merged['date'].dt.year.fillna(merged['date_oc'].dt.year).fillna(merged['date_ign'].dt.year)
merged_clean = merged.dropna(subset=['year']).copy()

# --- 3. HYPOTHESIS TESTING & SUMMARY ---
test_results = []

# H1: Metacritic Trend
df_h1 = merged_clean.dropna(subset=['critic_score', 'year'])
corr_meta, p_meta = pearsonr(df_h1['year'], df_h1['critic_score'])
test_results.append({'Hypothesis': 'H1: Critics vs Year', 'Stat': corr_meta, 'P-Value': p_meta})

# H2: Critic vs User Mean (Paired)
df_h2 = merged_clean.dropna(subset=['critic_score', 'user_score'])
t_stat, p_val_h2 = ttest_rel(df_h2['critic_score'], df_h2['user_score'])
test_results.append({'Hypothesis': 'H2: Critic vs User Mean', 'Stat': t_stat, 'P-Value': p_val_h2})

# H3: IGN Trend
df_h3 = merged_clean.dropna(subset=['critic_score_ign', 'year'])
corr_ign, p_ign = pearsonr(df_h3['year'], df_h3['critic_score_ign'])
test_results.append({'Hypothesis': 'H3: IGN vs Year', 'Stat': corr_ign, 'P-Value': p_ign})

# H4: Variance Comparison
stat_var, p_val_var = levene(df_h2['user_score'], df_h2['critic_score'])
test_results.append({'Hypothesis': 'H4: Variance (User vs Critic)', 'Stat': stat_var, 'P-Value': p_val_var})

# Display Results
print("\n" + "="*50)
print("HYPOTHESIS TEST SUMMARY")
print("="*50)
summary_df = pd.DataFrame(test_results)
summary_df['Significant?'] = summary_df['P-Value'] < 0.05
print(summary_df.to_string(index=False))


# --- 5. VISUALIZATIONS ---
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Graph 1: Trends Over Time (H1 & H3)
yearly_trends = merged_clean.groupby('year')[['critic_score', 'critic_score_ign']].mean()
sns.lineplot(data=yearly_trends, ax=axes[0,0], palette="magma", linewidth=2.5)
axes[0,0].set_title('Average Review Scores Over Time (0-100 Scale)')
axes[0,0].set_ylim(0, 100)

# Graph 2: Score Distributions (H2 & H4)
sns.kdeplot(merged_clean['critic_score'], label='Critics (Meta)', fill=True, ax=axes[0,1])
sns.kdeplot(merged_clean['user_score'], label='Users (Meta)', fill=True, ax=axes[0,1])
axes[0,1].set_title('Density of Review Scores')
axes[0,1].legend()

# Graph 4: Variance Comparison
df_melted = df_h2.melt(id_vars=['game'], value_vars=['critic_score', 'user_score'], 
                       var_name='Type', value_name='Score')
sns.boxplot(x='Type', y='Score', data=df_melted, ax=axes[1,1], palette="Set2")
axes[1,1].set_title('Spread of Scores: Critics vs. Users')

plt.tight_layout()
plt.show()

def top_discrepancies_per_year(
    df,
    n=5,
    critic_col='critic_score',
    user_col='user_score',
    year_col='year'
):
    paired = (
        df
        .dropna(subset=[critic_col, user_col, year_col, 'game'])
        .groupby([year_col, 'game'], as_index=False)
        .agg({
            critic_col: 'mean',
            user_col: 'mean'
        })
    )
    paired['score_diff'] = paired[critic_col] - paired[user_col]
    paired['abs_diff'] = paired['score_diff'].abs()
    top_n = (
        paired
        .sort_values([year_col, 'abs_diff'], ascending=[True, False])
        .groupby(year_col)
        .head(n)
        .reset_index(drop=True)
    )
    return top_n

def top_discrepancies_all_time(
    df,
    n=5,
    critic_col='critic_score',
    user_col='user_score'
):
    paired = (
        df
        .dropna(subset=[critic_col, user_col, 'game'])
        .groupby('game', as_index=False)
        .agg({
            critic_col: 'mean',
            user_col: 'mean'
        })
    )
    paired['score_diff'] = paired[critic_col] - paired[user_col]
    paired['abs_diff'] = paired['score_diff'].abs()

    top_n = (
        paired
        .sort_values('abs_diff', ascending=False)
        .head(n)
        .reset_index(drop=True)
    )
    return top_n

top_5_per_year = top_discrepancies_per_year(merged_clean, n=5)
top_5_all_time = top_discrepancies_all_time(merged_clean, n=5)

print("\n" + "="*60)
print("TOP 5 MOST CONTROVERSIAL GAMES PER YEAR")
print("="*60)
print(
    top_5_per_year[
        ['year', 'game', 'critic_score', 'user_score', 'score_diff']
    ].to_string(index=False)
)

print("\n" + "="*60)
print("TOP 5 MOST CONTROVERSIAL GAMES OF ALL TIME")
print("="*60)
print(
    top_5_all_time[
        ['game', 'critic_score', 'user_score', 'score_diff']
    ].to_string(index=False)
)
