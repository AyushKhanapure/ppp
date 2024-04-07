import pandas as pd

df = pd.read_csv("mtcars.csv")

print("Column Names:")
print(df.columns)

print("\n5th to 10th Rows:")
print(df.iloc[4:10])

print("\n4th to 7th Columns:")
print(df.iloc[:, 3:7])

num_rows, num_columns = df.shape
print("\nNumber of Rows:", num_rows)
print("Number of Columns:", num_columns)
