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