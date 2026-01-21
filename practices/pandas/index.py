
import pandas as pd
pd.set_option('display.max.columns',120)
pd.set_option('display.max.rows',100)
df=pd.read_csv(r"C:\Users\Mahendra\Downloads\customers-100.csv")
print(df.head(5))
df1=df[["Customer Id","City","Country"]]
# print(df1)
'''
df1.set_index("Country", inplace=True)
print(df1)
print(df1.loc["Solomon Islands"])
print(df[df["Country"]=="Solomon Islands"])'''

df1.set_index(["Country","City"], inplace=True)
df_sorted=df1.sort_index()
print(df_sorted)

print(df_sorted.loc["Solomon Islands"])
