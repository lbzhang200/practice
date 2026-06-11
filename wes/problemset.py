import numpy as np
import pandas as pd

employees = pd.DataFrame({
    "name":    ["Alice","Bob","Carol","Dan","Eve","Frank","Grace","Hiro"],
    "dept":    ["Eng","Eng","HR","HR","Eng","Finance","Finance","Eng"],
    "salary":  [95000, 88000, 72000, 68000, 102000, 85000, 91000, 77000],
    "years":   [3, 5, 2, 8, 1, 6, 4, 7],
    "rating":  [4.2, 3.8, 4.5, 3.1, 4.9, 4.0, 3.7, 4.3],
    "remote":  [True, False, False, True, True, False, True, False]
})

salaries = np.array([95000, 88000, 72000, 68000, 102000, 85000, 91000, 77000])

mean = salaries.mean()
sal_range = salaries.max() - salaries.min()
aboveavg = (salaries > mean).sum()
normalized = (salaries-salaries.min()) / sal_range 

salyear = np.array([
    [95000,3],[88000,5],[72000,2],[68000,8],
    [102000,1],[85000,6],[91000,4],[77000,7]
])

columnmean = salyear.mean(axis=0) #mean for columns (salary avg, years avg)
print(salyear.max(axis=1)) #max for each row
print(salyear.reshape(2, 8))
print(salyear.T)

salaries = np.array([95000, 88000, 72000, 68000, 102000, 85000, 91000, 77000])

above = salaries[salaries > 85000]
print(above)

salariescopy = salaries.copy()
salariescopy[salariescopy < 75000] = 750000
print(salariescopy)


#pandas problem set 
employees = pd.DataFrame({
    "name":    ["Alice","Bob","Carol","Dan","Eve","Frank","Grace","Hiro"],
    "dept":    ["Eng","Eng","HR","HR","Eng","Finance","Finance","Eng"],
    "salary":  [95000, 88000, 72000, 68000, 102000, 85000, 91000, 77000],
    "years":   [3, 5, 2, 8, 1, 6, 4, 7],
    "rating":  [4.2, 3.8, 4.5, 3.1, 4.9, 4.0, 3.7, 4.3],
    "remote":  [True, False, False, True, True, False, True, False]
})

print(employees["name", "salary"]) #prints name and salary columns
eng = employees[employees["dept"] == "Eng"]
print(eng)

topremote = employees[(employees["rating"] > 4.0) & (employees["remote"] == True)]
print(topremote)

df = employees.set_index("name")

print(df.loc["Alice", "salary"]) #row alice, column salary 
print(df.iloc[2, 1]) # row 3, col  1 - which is salary (since name is now the index)


print(df.loc["Bob": "Dan", "salary"])  #inclusive of both bob and dan + salary column
print(df.iloc[1:3]["salary"]) #exlusive position so bob, carol salary only 


#adding a column 

df = employees.copy()
df["level"] = df["years"].apply(
    lambda x: "senior"if x >= 5 else "junior"
)
df["total_comp"] = df["salary"] + (df["rating"] * 1000)
print(df.sort_values("total_comp", ascending=False))

#grouping

result = employees.groupby("dept").agg(
    avg_salary = ("salary", "mean")
    max_rating= ("rating", "max")
    headcount=("name", "count")
    remote_count=("remote","sum")
).reset_index()

print(result)

df = employees.copy()
df["dept_avg_salary"] = df.groupby("dept")["salary"].transform("mean")

df["vs_dept"] = df["salary"] - df["dept_avg"]
print(df.sort_values("vs_dept")[["name","dept","salary","dept_avg_salary", "vs_dept"]])

result = (
    employees[employees["years"] >= 3]
    .assign(bonus=lambda d: d["salary"] * 0.1)
    .groupby("dept")["bonus"]
    .sum()
    .reset_index()
    .sort_values("bonus", ascending=False)
    .rename(columns={"bonus": "total_bonus_budget"})
)
print(result)

