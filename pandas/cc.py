import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name":       ["Alice","Bob","Carol","Dave","Eve","Frank","Grace","Hank"],
    "dept":       ["Eng","Eng","Sales","Sales","HR","Eng","HR","Sales"],
    "salary":     [95000,88000,72000,67000,61000,105000,58000,74000],
    "years_exp":  [5,3,7,2,4,9,1,6],
    "rating":     [4.5,3.8,4.1,3.2,4.0,4.9,3.5,np.nan],
    "remote":     [True,False,True,False,True,False,True,False]
})

#get the salary column as a series

salary_df = df["salary"]
multiple_df = df[["name", "dept"]]

#get the index of 5 (Frank's row)
df.loc[5]
#last position 
df.iloc[-1]


#Get all employees in the Eng department. Then get everyone with a salary above 80,000.

df_employees = df[df["dept"] == "Eng" & (df["salary"] > 80000)]

#get all remote employees in the eng department

df[df["remote"] == True & df["dept"] == "Eng"]
df[df["salary"] >= 60000 & df["salary"] <= 80000]

#find which rows have a missing "rating"
df[df["rating"].isna()]
#fill missing values with mean rating of non-null rows 
df["rating"].fillna(df["rating"].mean())

#sort by salary descending
df.sort_values("salary", ascending=False)
#sort by dept ascending, then salary descending within each dept
df.sort_values(["dept", "salary"], ascending=[True, False])

#Add a column salary_k that shows salary in thousands (salary / 1000). 
df["salary_k"] = df["salary"] / 1000
# Then add a boolean column senior that is True when years_exp >= 5.
df["senior"] = df["years_exp"] >= 5


#Use apply to create a column level: "junior" if years_exp < 3, "mid" if 3–6, "senior" if > 6. Apply it row-wise.
def get_level(row):
    if row["years_exp"] < 3:
        return "junior" 
    elif row["years_exp"] <= 6:
        return "mid"
    else:
        return "senior"
df["level"] = df.apply(get_level, axis=1) #1 means row, 0 means column

#find mean salary per department
df["salary"].mean()

#find mean salary per department

df.groupby("dept")["salary"].mean() #groups by department, looks at salary column

#find total headcount and avg rating per department 
df.groupby("dept").agg({"salary": "count", "rating": "mean"})
#for multiple aggregations - headcount, and mean salary

#gives everyone in hr department a 10 percent salary raise 
df.loc[df["dept"] == "HR", "salary"] *= 1.1

#gets a frequency count of employees per department
df["dept"].value_counts()
df[["salary", "years_exp"]].describe()

#rename column_years to experience

df.rename(columns={"years_exp": "experience"})
df.drop(columns=["remote"])




