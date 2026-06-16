# =============================================================================
# PANDAS & NUMPY PRACTICE — Basics, Cleaning, Wrangling, Loading
# =============================================================================
# Instructions: work through each section top to bottom.
# Answer key is at the bottom — don't scroll until you've attempted it!
# Run this file in VS Code with the Python extension or Jupyter.
# =============================================================================

import pandas as pd
import numpy as np

# =============================================================================
# THE DATASET — a fake employee records table
# =============================================================================
# This is your data. All exercises below use this df.
# Run this block first so df is loaded before you start.

data = {
    "name":       ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Iris", "Jack"],
    "department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing", "Engineering", "HR", "Marketing", "Engineering", "HR"],
    "salary":     [95000, 72000, 88000, 61000, 75000, 102000, 58000, 69000, 91000, 63000],
    "age":        [29, 34, 41, 27, 38, 45, 31, None, 26, 52],
    "years":      [3, 7, 12, 2, 9, 18, 5, 4, 1, 14],
    "rating":     [4.2, 3.8, 4.5, 3.1, 4.0, 4.8, 2.9, 3.5, 4.1, None],
    "remote":     [True, False, True, False, True, False, True, False, True, False],
    "city":       ["NYC", "LA", "NYC", "Chicago", "LA", "NYC", "Chicago", "LA", "NYC", "chicago"],  # note the typo
}

df = pd.DataFrame(data)
print(df)
print()


# =============================================================================
# SECTION 1 — BASICS
# Goal: get comfortable inspecting and accessing data
# =============================================================================

# 1a. Print the first 5 rows of df

print(df.head())

# 1b. Print the shape of df (how many rows and columns?)

print(df.shape())

# 1c. Print the column names

print(df.columns)

# 1d. Print the data types of each column

print(df.dtypes)

# 1e. Print summary statistics for all numeric columns (count, mean, std, min, max)

print(df.descirbe())

# 1f. Select just the "name" and "salary" columns and print them

print(df["salary", "name"])

# 1g. Select all employees in the Engineering department

print(df[df["department"] == "Engineering"])


# 1h. Select all employees with a salary above 80000

print(df[df["salary"] > 80000])


# 1i. Select all employees in Engineering with salary above 85000

print(df[(df["department" == "Engineering"]) & (df["salary"] > 85000)])

# 1j. Print the salary of the employee named "Grace"
#     Hint: filter by name, then access the salary column
dfgrace = df[df["name"] == "Grace"]
gsalary = dfgrace["salary"].values[0]

# =============================================================================
# SECTION 2 — DATA CLEANING
# Goal: handle missing values, fix inconsistencies, fix types
# =============================================================================

# 2a. Find how many missing values are in each column

print(df.isnull().sum())

# 2b. Fill the missing "age" value with the mean age of all other employees
#     Hint: df["age"].mean()

df["age"] = df["age"].fillna(df["age"].mean())

# 2c. Fill the missing "rating" value with the median rating
#     Hint: df["rating"].median()

df["rating"] = df["rating"].fillna(df["rating"].median())


# 2d. The "city" column has an inconsistency — "chicago" should be "Chicago"
#     Fix it so all city values are properly capitalized
#     Hint: .str.capitalize() or .str.title()

df["city"] = df["city"].str.title()

# 2e. Confirm there are no more missing values — print the null counts again

print(df.isnull().sum())

# 2f. The "age" column is float after the fill. Convert it to int.
#     Hint: .astype(int)

df["age"] = df["age"].astype(int)

# =============================================================================
# SECTION 3 — DATA WRANGLING
# Goal: reshape, group, sort, add columns, and summarize
# =============================================================================

# 3a. Sort the dataframe by salary from highest to lowest

print(df.sort_values("salary", ascending=False))

# 3b. Add a new column called "salary_k" that shows salary in thousands
#     e.g. 95000 → 95.0
#     Hint: divide by 1000

df["salary_k"] = df["salary"] / 1000


# 3c. Add a new column called "senior" that is True if years >= 10, False otherwise
#     Hint: df["years"] >= 10

df["senior"] = df["years"] >= 10 

# 3d. Group by department and find the average salary per department

print(df.groupby("department")["salary"].mean())

# 3e. Group by department and find:
#     - average salary
#     - max rating
#     - count of employees
#     Hint: .agg({"salary": "mean", "rating": "max", "name": "count"})

print(df.groupby("department").agg({
                "salary" : "mean", 
                "rating" : "max", 
                "name" : "count"
}))

# 3f. Find the highest paid employee in each department
#     Hint: use groupby + idxmax to get the index, then loc
idx = df.groupby("department")["salary"].idxmax() 
print(df.loc[idx][["department", "name", "salary"]])

# 3g. Find the total salary spend per department

print(df.groupby("department")["salary"].sum())

# 3h. Filter to only remote workers, then show their names and salaries

remote_workers = df[df["remote"] == True][["name", "salary"]]
print(remote_workers)

# 3i. Add a column "salary_band" based on salary:
#     "low"    if salary < 70000
#     "mid"    if 70000 <= salary < 90000
#     "high"   if salary >= 90000
#     Hint: use pd.cut() or np.select()

conditions = [df["salary"] < 70000, 
              70000 <= df["salary"] < 90000, 
              df["salary"] >= 90000]
options = ["low", "mid", "high"]

df["salary_band"] = np.select(conditions, options)

# 3j. Show the count of employees in each salary_band

print(df["salary_band"].value_counts())

# =============================================================================
# SECTION 4 — NUMPY
# Goal: practice array operations, math, and masking
# =============================================================================

# Use this array for 4a-4h
scores = np.array([88, 92, 79, 95, 61, 74, 83, 90, 55, 100, 67, 78])

# 4a. Print the mean, median, and standard deviation of scores

print(np.mean(scores), np.median(scores), np.std(scores))

# 4b. Print the max and min scores

print(np.max(scores), np.min(scores))

# 4c. Find all scores above 80 using a boolean mask

print(scores[scores > 80])

# 4d. Count how many scores are above 80

print(scores[scores > 80].sum())

# 4e. Normalize scores to a 0-1 scale
#     Formula: (score - min) / (max - min)

print(scores - scores.min()) / (scores.max() - scores.min())

# 4f. Replace any score below 60 with 60 (the minimum passing score)
#     Hint: scores[scores < 60] = 60   (works in-place on a copy)

scores_copy = scores.copy()
scores_copy[scores_copy < 60] = 60
print(scores_copy)

# 4g. Reshape scores into a 3x4 matrix
#     Hint: .reshape(3, 4)

print(scores.reshape(3,4))


# 4h. Find the mean score per row in the reshaped matrix
#     Hint: .mean(axis=1)

print(scores.mean(axis=1))

# Use this 2D array for 4i-4j
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 4i. Print the sum of each column
#     Hint: axis=0 goes down the rows (column-wise)

print(scores.sum(axis = 0)) #each column 

# 4j. Print the sum of each row
#     Hint: axis=1 goes across columns (row-wise)

print(scores.sum(axis = 1))

# =============================================================================
# SECTION 5 — LOADING (read and write)
# Goal: practice saving and loading data
# =============================================================================

# 5a. Save df to a CSV file called "employees.csv" (no index)
#     Hint: df.to_csv("employees.csv", index=False)

df.to_csv("employees.csv", index=False)

# 5b. Load it back from the CSV into a new variable called df_loaded

df_loaded = pd.read_csv("employees.csv")

# 5c. Confirm df_loaded looks the same as df — print its head

print(df_loaded)
print(df)

# 5d. Save df to a JSON file called "employees.json"
#     Hint: df.to_json("employees.json", orient="records", indent=2)

df.to_json("employees.json", orient = "records", indent= 2)

# 5e. Load the JSON back into df_json and print its shape

df_loaded = pd.read_json("employees.json")
print(df_loaded.shape)
# =============================================================================
#
#
#
#   ANSWER KEY — scroll down only after attempting each section!
#
#
#
# =============================================================================
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# =============================================================================
# ANSWER KEY
# =============================================================================

import pandas as pd
import numpy as np

data = {
    "name":       ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Iris", "Jack"],
    "department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing", "Engineering", "HR", "Marketing", "Engineering", "HR"],
    "salary":     [95000, 72000, 88000, 61000, 75000, 102000, 58000, 69000, 91000, 63000],
    "age":        [29, 34, 41, 27, 38, 45, 31, None, 26, 52],
    "years":      [3, 7, 12, 2, 9, 18, 5, 4, 1, 14],
    "rating":     [4.2, 3.8, 4.5, 3.1, 4.0, 4.8, 2.9, 3.5, 4.1, None],
    "remote":     [True, False, True, False, True, False, True, False, True, False],
    "city":       ["NYC", "LA", "NYC", "Chicago", "LA", "NYC", "Chicago", "LA", "NYC", "chicago"],
}

df = pd.DataFrame(data)


# --- SECTION 1 ---

# 1a
print(df.head())

# 1b
print(df.shape)                         # (10, 8)

# 1c
print(df.columns.tolist())

# 1d
print(df.dtypes)

# 1e
print(df.describe())

# 1f
print(df[["name", "salary"]])

# 1g
print(df[df["department"] == "Engineering"])

# 1h
print(df[df["salary"] > 80000])

# 1i
print(df[(df["department"] == "Engineering") & (df["salary"] > 85000)])

# 1j
print(df[df["name"] == "Grace"]["salary"].values[0])   # 58000


# --- SECTION 2 ---

# 2a
print(df.isnull().sum())

# 2b
df["age"] = df["age"].fillna(df["age"].mean())

# 2c
df["rating"] = df["rating"].fillna(df["rating"].median())

# 2d
df["city"] = df["city"].str.title()     # "chicago" → "Chicago"

# 2e
print(df.isnull().sum())                # all zeros now

# 2f
df["age"] = df["age"].astype(int)


# --- SECTION 3 ---

# 3a
print(df.sort_values("salary", ascending=False))

# 3b
df["salary_k"] = df["salary"] / 1000

# 3c
df["senior"] = df["years"] >= 10

# 3d
print(df.groupby("department")["salary"].mean())

# 3e
print(df.groupby("department").agg({
    "salary": "mean",
    "rating": "max",
    "name":   "count"
}))

# 3f
idx = df.groupby("department")["salary"].idxmax()
print(df.loc[idx][["department", "name", "salary"]])

# 3g
print(df.groupby("department")["salary"].sum())

# 3h
remote_workers = df[df["remote"] == True][["name", "salary"]]
print(remote_workers)

# 3i
conditions = [
    df["salary"] < 70000,
    (df["salary"] >= 70000) & (df["salary"] < 90000),
    df["salary"] >= 90000
]
choices = ["low", "mid", "high"]
df["salary_band"] = np.select(conditions, choices)

# 3j
print(df["salary_band"].value_counts())


# --- SECTION 4 ---

scores = np.array([88, 92, 79, 95, 61, 74, 83, 90, 55, 100, 67, 78])

# 4a
print(np.mean(scores), np.median(scores), np.std(scores))

# 4b
print(np.max(scores), np.min(scores))

# 4c
print(scores[scores > 80])

# 4d
print(np.sum(scores > 80))              # count of True values

# 4e
normalized = (scores - scores.min()) / (scores.max() - scores.min())
print(normalized.round(2))

# 4f
scores_copy = scores.copy()
scores_copy[scores_copy < 60] = 60
print(scores_copy)

# 4g
matrix_scores = scores.reshape(3, 4)
print(matrix_scores)

# 4h
print(matrix_scores.mean(axis=1))       # mean of each row

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 4i
print(matrix.sum(axis=0))              # [120, 150, 180]

# 4j
print(matrix.sum(axis=1))              # [60, 150, 240]


# --- SECTION 5 ---

# 5a
df.to_csv("employees.csv", index=False)

# 5b
df_loaded = pd.read_csv("employees.csv")

# 5c
print(df_loaded.head())

# 5d
df.to_json("employees.json", orient="records", indent=2)

# 5e
df_json = pd.read_json("employees.json")
print(df_json.shape)