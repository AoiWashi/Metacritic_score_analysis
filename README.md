# Metacritic Score Analysis

This project collects and analyzes video game ratings from **Metacritic** to test several hypotheses for my DSA 210 term project.  
The goal is to explore how critic (expert) scores and user (player) scores differ, and how these patterns change over time.

---

## Project Goals
- Collect structured game rating data from Metacritic  
- Clean and organize the dataset  
- Analyze score trends by year  
- Compare critic vs. user scoring behavior  
- Visualize results using charts and graphs  

---

## Data Collection Method

I will gather data from Metacritic using a Python web-scraping script.

The dataset will include:

- **Game title**  
- **Release date**  
- **Developer**  
- **Publisher**  
- **Critic (expert) score**  
- **User (player) score**  
- **Number of critic reviews** (if available)  
- **Number of user ratings** (if available)

This data will be saved into a CSV file for analysis.

---

## Hypotheses

### **Hypothesis 1**  
**Experts give higher scores in recent years than before.**  
I will test this by comparing average critic scores across release years.

### **Hypothesis 2**  
**Players give lower scores than experts.**  
I will check this by comparing the average user score to the critic score for each game.

---

## Tools & Libraries
The project will use:

- Python  
- BeautifulSoup4  
- Requests  
- Pandas  
- Matplotlib / Seaborn (for graphs)  
