import pandas as pd
df1 = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
        # "Amount" :[1.0,2.5,4.5]
    }
)

df2 = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["M", "male", "female"],
    }
)
print(df1)
print(df2)

print()
print("align_axis=False")
comp=df1.compare(df2,align_axis=False,keep_equal=False,keep_shape=False)
print(comp)
print("align_axis=True")
comp=df1.compare(df2,align_axis=True,keep_equal=True,keep_shape=True)
print(comp)
print("align_axis Default")
comp=df1.compare(df2)
print(comp)
