# 📊 Final Analysis & Research Findings

This section summarizes the results of the statistical tests conducted on the combined datasets from **Metacritic**, **OpenCritic**, and **IGN**.

---

## 1. Hypothesis Testing Results

### **Hypothesis 1: Expert Score Inflation**
> *Experts give higher scores in recent years than in the past.*
* **Method:** Pearson Correlation Coefficient ($r$) between `year` and `critic_score`.
* **Result:** r = -0.014604 This shows a very slight negative correlation.
* **Finding:** Contrary to the idea of "review inflation," data suggests that as time goes on, critic scores have actually dropped by a tiny amount. Because the P-Value is so small (1.81 \times 10^-37), this tiny downward trend is mathematically real, not a fluke..

### **Hypothesis 2: Critic vs. User Sentiment**
> *Players give lower scores than expert reviewers on average.*
* **Method:** Paired T-Test comparing normalized Critic Scores vs. User Scores.
* **Result:** t = 655.02$, p = 0.0 Hypothesis Supported.
* **Finding:** A T-stat of 655 is massive. This confirms that there is a giant, consistent gap where critics score games higher than users. The P-value of 0.0 means the probability that this gap is a mistake is zero.


### **Hypothesis 3: IGN Specific Trends**
> *IGN gives higher scores in recent years than in the past.*
* **Method:** Pearson Correlation specifically for the IGN dataset.
* **Result:** IGN vs Year Stat = 0.049105 p = 4.664288e-244 Hypothesis Supported.
* **Finding:** Unlike the general critic pool (H1), IGN’s scores are actually rising over time (r is positive). While the rise is small, the P-value (4.66 \times 10^{-244}) is so low that it confirms IGN has a specific trend of giving slightly higher scores in recent years.

### **Hypothesis 4: The Variance Gap (Polarization)**
> *The variance of user scores is higher than critic scores.*
* **Method:** Levene’s Test for Equality of Variances.
* **Result:** Variance (User vs Critic) W = 132740.69, p = 0.0 Hypothesis Supported.
* **Finding:** This is strongest result. The variance of users is significantly higher than critics. This mathematically proves that users are "unpredictable" and "extreme" (using 0s and 10s), while critics are "stable" and "conservative" (staying in the 70-80 range).

---

## 2. Visualization Analysis

### **Distribution of Scores**
Our density plots (KDE) show that Critic scores follow a **Normal Distribution** (bell curve), while User scores are **Skewed** and show more "noise" at the lower end of the spectrum.
![Image](Figure_1.png)

## 🏆 The "Controversy Gap": Top 5 Most Disputed Titles

The following table identifies games with the largest absolute discrepancy between professional critics and the general public. These titles represent significant "Review Bombing" incidents or major disconnects between technical quality and player satisfaction.

| Game Title | Critic Score | User Score | Controversy Gap |
| :--- | :---: | :---: | :---: |
| **Tom Clancy's The Division 2: Warlords of New York** | 79.0 | 9.0 | **70.0** |
| **Diablo IV** | 86.0 | 20.0 | **66.0** |
| **Overwatch 2** | 79.0 | 14.0 | **65.0** |
| **The Sims 4: Star Wars - Journey to Batuu** | 70.0 | 11.0 | **59.0** |
| **FIFA 21** | 74.0 | 15.0 | **59.0** |

---

### 🔍 Analysis of Outliers
1. **The "Live Service" Effect:** Almost all games in the Top 5 are "Live Service" titles or expansions. The high gap is often caused by post-launch monetization, server issues, or balance changes that critics (who review the launch version) don't weight as heavily as daily players.
2. **Extreme Disparity:** A gap of **70.0 points** (as seen in *The Division 2*) is statistically extreme. In these cases, the `user_score` is rarely a reflection of the game's art or mechanics, but rather a form of "protest voting."
3. **Hypothesis Link:** This list provides qualitative proof for **Hypothesis 4**. The fact that users gave a 9.0/100 while critics gave a 79/100 demonstrates the high variance and polarization found in player datasets.
                                          
### **Annual Controversy**
Using `top_discrepancies_per_year` function, identified the most "divisive" games by year.
There are so many games so I did not at them here

---

## 3. Final Conclusion
The data supports the conclusion that **Critics and Players utilize different evaluation frameworks.** Critics focus on technical execution and industry standards, while users respond more to emotional resonance and post-launch performance. The high variance in user scores confirms that the gaming community is more polarized than the professional review circle.

---
**Project by:** [Your Name]  
**Course:** DSA210 – Introduction to Data Science  
**Term:** Fall 2025
