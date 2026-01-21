import pandas as pd

# Create DataFrame
data={ 
    'student':["Mahendra","Surekha","Roshan","Sathwik"],
    'rank':[1,2,3,4],
    'marks':[50,80,85,90]
}
student=pd.DataFrame(data)
print(student)

# Access group of rows using index
print()
print(student.loc[0])

# Access group of rows using index
print()
print(student.iloc[[2,1]])
