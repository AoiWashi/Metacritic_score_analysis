# 🤖 7. Machine Learning Extension: Sentiment Clustering

### Objective
To move beyond basic statistical summaries, I implemented an **Unsupervised Machine Learning** model using **K-Means Clustering**. The goal is to let the algorithm mathematically identify natural groups of games based on the relationship between `critic_score` and `user_score`.

### Methodology
1. **Feature Selection:** We use the two normalized score columns as our primary features.
2. **Feature Scaling:** Since K-Means relies on Euclidean distance, we apply `StandardScaler` to ensure that both scoring axes are treated with equal weight.
3. **Hyperparameters:** We set $K=4$ clusters to represent the four quadrants of reception: Unanimous Success, The Controversy Zone, Hidden Gems, and General Flops.

---

### Implementation Code
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from IPython.display import display

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

# 1. Select the relevant features for the ML model
# We use the 'merged_clean' dataframe created in Section 2
ml_data = merged_clean[['critic_score', 'user_score']].dropna()

# 2. Scaling (Important for K-Means)
# This ensures that one axis doesn't 'overpower' the other
scaler = StandardScaler()
scaled_features = scaler.fit_transform(ml_data)

# 3. Applying K-Means Clustering
# We choose K=4 to represent the four quadrants of game reception
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42, n_init=10)
ml_data['cluster'] = kmeans.fit_predict(scaled_features)

# 4. Visualizing the ML Results
plt.figure(figsize=(12, 7))
scatter = sns.scatterplot(
    data=ml_data, 
    x='critic_score', 
    y='user_score', 
    hue='cluster', 
    palette='viridis', 
    alpha=0.6,
    edgecolor='w'
)



plt.title('Machine Learning Results: Sentiment Clustering', fontsize=15)
plt.xlabel('Critic Score (Standardized)', fontsize=12)
plt.ylabel('User Score (Standardized)', fontsize=12)
plt.legend(title='Sentiment Cluster')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```
# 5. Descriptive Statistics for each Cluster
print("SUMMARY PER CLUSTER:")
cluster_summary = ml_data.groupby('cluster').agg(['mean', 'count']).round(2)
display(cluster_summary)
