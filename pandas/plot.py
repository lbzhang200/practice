from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

script_dir = Path(__file__).resolve().parent
csv_path = script_dir / 'data.csv'

if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_path}")
if csv_path.stat().st_size == 0:
    raise ValueError(f"CSV file is empty: {csv_path}")

df = pd.read_csv(csv_path)
df.plot()
plt.show()

# make a scatter plot
df.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

#histogram 

df["Duration"].plot(kind = 'hist')

