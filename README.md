# Video Game Review Score Analysis  
### Comparing Metacritic • OpenCritic • IGN

This project collects and analyzes video game review scores from **Metacritic**, **OpenCritic**, and **IGN** to explore how review patterns differ across platforms and over time.  
By combining multiple datasets, the project provides a broader and more accurate understanding of how games are rated by critics and players.

---

## Motivation

I have always enjoyed playing video games, and I regularly check game reviews before deciding what to play next.  
Over time, I noticed that different review platforms—such as **Metacritic**, **OpenCritic**, and **IGN**—often give different scores for the same game. This made me curious:

- Why do these differences happen?  
- Are some platforms consistently harsher or more generous?  
- Do critic and user reviews follow the same patterns?

Since I enjoy both gaming and data analysis, this project lets me combine these interests.  
Using multiple datasets allows me to compare rating systems more accurately and understand:

- How critic and user scores differ  
- How review trends change over time  
- Which platforms align or disagree the most  

This project is both personally interesting and academically valuable.

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

### **Metacritic**
Includes:
- Critic (expert) score
- User (player) score
- Release date
- Developer / Publisher

### **OpenCritic**
Includes:
- Top Critic score
- Player rating
- Platforms listed

### **IGN**
Includes:
- IGN numeric score
- Reviewer
- Game genre & release information

---

## Hypotheses

### **Hypothesis 1:**  
**Experts give higher scores in recent years than in the past.**

### **Hypothesis 2:**  
**Players give lower scores than expert reviewers on average.**

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

---

## Data Collection Scripts

All scraping code is stored in:  
