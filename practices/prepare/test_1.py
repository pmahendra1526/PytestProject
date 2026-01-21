
def poliydrome(value):
    return value==value[::-1]

word="MAHI"
print(f"Word {word} is polindrome - {poliydrome(word)}")

import pandas as pd

df=pd.read_csv(r"C:\Users\Mahendra\Desktop\status.csv")
df['Status']=df['Status'].str[0]
print(df)

print()
print(df['Status'].str[0])

