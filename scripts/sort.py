import pandas as pd

x = pd.read_csv("data/electricity.csv")
x.sort_values(
    by=['year', 'parameter', 'carrier', 'tech', 'source'], inplace=True)

x = x[['year', 'parameter', 'carrier', 'tech', 'value', 'unit', 'source']]
x.to_csv("data/electricity.csv", index=False)
