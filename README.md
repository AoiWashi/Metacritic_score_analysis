# Video Game Review Score Analysis  
### Comparing Metacritic • OpenCritic • IGN

This project collects and analyzes video game review scores from **Metacritic**, **OpenCritic**, and **IGN** to explore how review patterns differ across platforms and over time.  
By combining multiple datasets, the project provides a broader and more accurate understanding of how games are rated by critics and players.

---

## Motivation

As someone who follows video game reviews closely, I've always noticed that the same game can receive very different scores depending on where you look. Sometimes critics love a game while players dislike it — or the opposite. This made me curious:

- Do critics and players judge games differently?
- How have review patterns changed over the years?

This project is my attempt to answer these questions using real data. By combining multiple review platforms, I hope to better understand how games are rated and what these differences reveal about both the gaming community and the industry as a whole.

---

## Project Goals

- Collect and combine game rating data from **Metacritic**, **OpenCritic**, and **IGN**
- Clean and standardize datasets from multiple sources
- Compare critic vs. user scoring behavior across platforms
- Analyze score trends over time
- Produce visualizations for clear comparison  
- Test hypotheses related to review behavior

---

## Data Sources

| # | Data Type        | Source | Description |
|---|------------------|---------|-------------|---------------|
| 1 | Metacritic   | https://www.kaggle.com/datasets/beridzeg45/metacritic-pc-games-reviews/data | Core game data: title, release date, developer, platforms, metascore, user rating |
| 2 | OpenCritic   | https://www.kaggle.com/code/nazilkabaz/web-scraping-from-open-critic/output | Used for comparison |
| 3 | IGN   | https://www.kaggle.com/code/advancedforestry/ign-score-analytics/input | To check biggest reviwer site |

---

## Hypotheses

### **Hypothesis 1:**  
**Experts give higher scores in recent years than in the past.**

### **Hypothesis 2:**  
**Players give lower scores than expert reviewers on average.**

### **Hypothesis 2:**  
**IGN give higher score in recent years than in the past.**

### **Hypothesis 4:**  
**The variance of user scores is higher than critic scores.**  
Users tend to be more extreme in their ratings.

---

## Tools & Technologies

- **Python**  
- **Requests + BeautifulSoup4** (scraping)
- **Pandas** (cleaning + merging)
- **NumPy** (statistics)
- **Matplotlib / Seaborn** (visualizations)
- **Jupyter Notebook** (analysis)
