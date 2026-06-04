# Student Performance Factors: A Data Visualization Project

This is my project for the GDV module (Fundamentals of Data Visualization, FS26).

**Research question:** Which factors have the greatest influence on student exam performance?

I worked with a synthetic student performance dataset from Kaggle and built three visualizations covering different angles of the question: learning habits, social and family factors, and personal motivation. Each chart appears twice in the project, once as I originally designed it and once after revising it based on user feedback from a Think-Aloud evaluation. The full design rationale and the reasoning behind every change are in the report.

## Repository structure

```
.
├── data/
│   ├── StudentPerformanceFactors.csv         # raw data, downloaded from Kaggle
│   └── data_cleaned.csv                      # cleaned data, produced by the exploration notebook
├── notebooks/
│   ├── Exploration/
│   │   ├── 01_exploration.ipynb              # data cleaning, basic stats, correlation analysis
│   │   ├── eda_report.html                   # auto-generated EDA report
│   │   └── eda_report.py                     # script that generates the EDA report
│   ├── Pre Evaluation/
│   │   └── 02_visualizations.ipynb           # the three charts BEFORE user feedback
│   └── Evaluation/
│       └── 02_visualizations_improved.ipynb  # the same three charts AFTER user feedback
├── LICENSE
└── README.md
```

## How to run

1. Clone or download this repository.
2. Make sure you have Python 3.11 (or newer) installed.
3. Install the required packages:

   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

4. Run the notebooks in this order:

   1. `notebooks/Exploration/01_exploration.ipynb`. This is the starting point. It reads the raw CSV, drops rows with missing values, and writes the cleaned dataset to `data/data_cleaned.csv`.
   2. `notebooks/Pre Evaluation/02_visualizations.ipynb`. Produces the three charts in their original (pre-evaluation) form.
   3. `notebooks/Evaluation/02_visualizations_improved.ipynb`. Produces the same three charts in their revised (post-evaluation) form.

Each visualization notebook reads from `data/data_cleaned.csv`, so the exploration notebook needs to be run first.

## Dataset

The dataset is *StudentPerformanceFactors* from Kaggle, uploaded by the user *lainguyn123*. It is synthetically generated and contains 6,607 rows across 20 columns covering demographic, behavioral, and academic factors. After dropping rows with missing or empty values, 6,378 rows remain.

The target variable is `Exam_Score`. The factors most discussed in this project are `Attendance`, `Family_Income`, and `Motivation_Level`.

Source: https://www.kaggle.com/datasets/lainguyn123/student-performance-factors

## Deliverables

- **Report (PDF):** dataset description, design rationale, evaluation methodology, design improvements, and references.
- **Pitch slides (PDF):** 5-minute final presentation.
- **Notebooks:** the three notebooks listed above contain all the code used to produce the figures in the report and slides.

## Tools

- Python 3.11
- pandas, numpy for data handling
- matplotlib, seaborn for the visualizations
- Jupyter Notebook

---

*Project for the Fundamentals of Data Visualization (GDV) module, Spring Semester 2026.*
