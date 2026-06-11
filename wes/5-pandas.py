import pandas as pd
#pandas is better than numpy because it works with labels and data rather than just integers 


pop = pd.Series([35000, 71000, 16000],
                index=["Ohio", "Texas", "Oregon"])

#functinos like a dictionary kind of 
pop["Ohio"]  # 35000
pop[pop > 20000] #Ohio: 35000, Texas: 71000
pop * 2 #double all values 

# from a dict
s = pd.Series({"Ohio": 35000, "Texas": 71000})

# useful attributes
s.index      # Index(['Ohio', 'Texas'])
s.values     # array([35000, 71000])
s.dtype      # int64
s.name       # optional label for the series


#read csv 

df = pd.read_csv("data.csv")

#data frame stuff 

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Carol", "Dan"],
    "dept":   ["Eng", "Eng", "HR", "HR"],
    "salary": [90000, 85000, 72000, 68000],
    "years":  [3, 5, 2, 8]
})

#important functions 
df.shape          # (4, 4)
df.dtypes         # column types
df.head(2)        # first 2 rows
df.tail(2)        # last 2 rows
df.info()         # summary of columns + nulls
df.describe()     # stats: mean, std, min, max, etc.

df["salary"]      # → Series (one column)
df[["name","salary"]]   # → DataFrame (multiple cols)
df["bonus"] = df["salary"] * 0.1  # new column
del df["bonus"]   # remove column

#indexing in pandas 
df = pd.DataFrame({
    "name": ["Alice","Bob","Carol"],
    "salary": [90000, 85000, 72000]
}, index=["a","b","c"])

#.loc - use only index labels 
df.loc["a"] #row with label "a"
df.loc["a", "salary"] #90000 #a row and salary column 
df.loc["a": "b", "salary"] #both endpoints included (inclusive)

#.iloc - use integer positions 
df.iloc[0] #first row position zero 
df.iloc[0, 1] #row 0, col 1 --> 900000
df.iloc[0:2, :] #rows 0-1, all cols #end exlucded) - normal 

#filtering 
df = pd.DataFrame({
    "name":   ["Alice","Bob","Carol","Dan"],
    "dept":   ["Eng","Eng","HR","HR"],
    "salary": [90000,85000,72000,68000]
})


df[df["salary"] > 75000] #filter for salary > 75000

df[(df["dept"]=="Eng") & (df["salary"] > 80000)] #multiple conditions 
#use &, | not and/or

#use isin to match against a list 
df[df["dept"].isin(["Eng", "Finance"])]

# isna/notna - find missing vlaues 
df[df["salary"].isna()]
df[df["salary"].notna()]

#string matching 
df[df["name"].str.startswith("A")]

#adding columns 

df["level"] = df["salary"].apply(
    lambda x: "senior" if x > 80000 else "junior"
)

# apply row-wise (axis=1)
df["combo"] = df.apply(
    lambda row: f"{row['name']} ({row['dept']})", axis=1
)

#Group values 

df.groupby("dept")["salary"].mean()

#dept groups by department then calculates the mean for salaries
#Eng 87500.0 
#HR 70000.0 

df.groupby("dept")["salary"].agg(["mean","max","count"]) #can make multiple aggregations at once: mean, max, count

df.groupby(["dept","level"])["salary"].mean()

df.groupby(["dept","level"])["salary"].mean() #multiple group keys 

#sort values by index 
df.sort_values("salary", ascending=False) #sort by column of salary 
df.sort_values(["dept", "salary"]) #multi column sort first sort by department, then salary 
df.sort_index() #sort by row index, helps with restoring original row order 

#ranking
df["rank"] = df["salary"].rank(ascending=False)

df.isna().sum() #count nan per column
df.dropna() #drop rows with any nan
df.dropna(subset=["salary"]) #only drop is salary is nan
df.fillna() #replace nan values with zero 
df["salary"].fillna(df["salary"].mean()) #fills nan values with mean 




#series vs dataframe 
df["salary"]        # → Series (1D)
df[["salary"]]      # → DataFrame (2D, one column)

# matters when you call methods that expect one type
df["salary"].mean()       # works
df[["salary"]].mean()     # also works but returns a DataFrame