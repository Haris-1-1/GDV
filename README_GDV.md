# Student Performance Factors: A Data Visualization Project

This is my project for the GDV module (Fundamentals of Data Visualization, FS26).

**Research question:** Which factors have the greatest influence on student exam performance?

I worked with a synthetic student performance dataset from Kaggle and built three visualizations covering different angles of the question: learning habits, social and family factors, and personal motivation. Each chart exists in two versions, one as I first designed it and one after revising it based on user feedback from a Think-Aloud evaluation with four participants. The full design rationale and the reasoning behind every change are in `GDV-Final.pdf`.

## Repository structure

```
.
├── Data-Visualization/
│   ├── data/
│   │   ├── StudentPerformanceFactors.csv        # raw data, downloaded from Kaggle
│   │   └── data_cleaned.csv                     # cleaned data, produced by the 
│   └── Notebooks/
│       ├── Exploration/
│       │   ├── 01_exploration mainy.ipynb       # data cleaning, basic stats, 
│       │   ├── eda_report.html                  # auto-generated EDA report
│       │   └── eda_report.py                    # script that produces the EDA report
│       ├── Pre-Evaluation/
│       │   └── 02_visualizations pre.ipynb      # the three charts BEFORE user 
│       └── Evaluation/
│           └── 02_visualizations_improved_3.ipynb   # the same three charts AFTER 
├── Survey-Evaluation/
│   ├── README.md                                # explains the evaluation setup
│   ├── task_description.md                      # tasks shown to the participants
│   ├── survey_form.md                           # the form used during the 
│   ├── P1_notes.md                              # notes from participant 1
│   ├── P2_notes.md                              # notes from participant 2
│   ├── P3_notes.md                              # notes from participant 3
│   └── P4_notes.md                              # notes from participant 4
├── GDV-Final.pdf                                # the final written report
├── final pitch.pdf                              # the slides used for the 5-minute 
├── LICENSE
└── README GDV.md                                # this file
```

> Note: the folder name is `Data-Vizualization` (missing an "s", typo on my side).

## How to run the code

1. Clone or download this repository.
2. Make sure you have Python 3.11 or newer installed.
3. Install the required packages:

   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

4. Run the notebooks in this order. All of them live under `Data-Vizualization/Notebooks/`:

   1. `Exploration/01_exploration mainy.ipynb`. Reads the raw CSV from `Data-Vizualization/data/StudentPerformanceFactors.csv`, drops rows with missing values, and writes the cleaned dataset to `Data-Vizualization/data/data_cleaned.csv`. Also produces the correlation table used to pick the three sub-topics.
   2. `Pre-Evaluation/02_visualizations pre.ipynb`. Produces the three charts in their original (pre-evaluation) form.
   3. `Evaluation/02_visualizations_improved_3.ipynb`. Produces the same three charts in their revised (post-evaluation) form.

Both visualization notebooks read from `Data-Vizualization/data/data_cleaned.csv`, so the exploration notebook needs to run first.

The Exploration folder also contains `eda_report.html` and `eda_report.py`. The HTML file is an auto-generated overview of the dataset (distributions, missing values, correlations) and is not required for reproducing the charts. To regenerate it, run `python eda_report.py`.

## Dataset

The dataset is *StudentPerformanceFactors* from Kaggle, uploaded by the user *lainguyn123*. It is synthetically generated and contains 6,607 rows across 20 columns covering demographic, behavioral, and academic factors. After dropping rows with missing or empty values, 6,378 rows remain.

The target variable is `Exam_Score`. The three factors discussed in this project are `Attendance`, `Family_Income`, and `Motivation_Level`.

Source: https://www.kaggle.com/datasets/lainguyn123/student-performance-factors

## Evaluation materials

The `Survey-Evaluation/` folder contains everything needed to reproduce the user evaluation:

- `task_description.md`: the tasks each participant was asked to complete while looking at the three charts.
- `survey_form.md`: the questions and the rating scale used during the think-aloud sessions.
- `P1_notes.md` to `P4_notes.md`: anonymised notes taken during each session. Names are removed, only the role of the participant is kept (two fellow students, one family member, one friend).
- `README.md`: short summary of how the evaluation was run and how the notes are structured.

## Deliverables

- **Report (PDF):** `GDV-Final.pdf`. Contains dataset description, design rationale, evaluation methodology, design improvements, references, and figures.
- **Pitch slides (PDF):** `final pitch.pdf`. The 5-minute final presentation.
- **Notebooks:** the three notebooks listed above contain all the code used to produce the figures in the report and slides.
- **Evaluation materials:** everything in the `Survey-Evaluation/` folder.

## Tools

- Python 3.11
- pandas, numpy for data handling
- matplotlib, seaborn for the visualizations
- Jupyter Notebook for the analysis

---

*Project for the Fundamentals of Data Visualization (GDV) module, Spring Semester 2026.*
*Author: Haris Salii*
