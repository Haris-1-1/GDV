import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data/StudentPerformanceFactors.csv')
df = df.replace('', pd.NA).dropna()

print(f"Rows after cleaning: {len(df)}")

profile = ProfileReport(df, title="Student Performance Factors, EDA Report", explorative=True)
profile.to_file("eda_report.html")

print("Done, report saved as eda_report.html")
