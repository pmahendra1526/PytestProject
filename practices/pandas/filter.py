import pandas as pd
# pd.set_option('display.max.rows',1000)
# pd.set_option('display.max.columns',10)
names=["Name","Gender","StartDate","LastOriginTime","Salary","Bonus","SrMgmt","Team"]
emp=pd.read_csv("C:\\Users\\Mahendra\\Downloads\\employees.csv",skiprows=1,names=names)

print(emp.head())

# print("######## Filter Data ########")
# print(emp[emp["Salary"] >= 149000])
# print()
# filter_Name=['Kathy','Russell']
# print(emp[emp["Name"].isin(filter_Name)])

# print(emp[emp["Name"].str.contains('Russell',na=False)])

# Set Index
emp1=emp.set_index("Team")
print(emp1.head(5))
# print(emp1.filter(items=["Gender","Names"],axis=1)) # columns we want to keep

print(emp1.iloc[3])

# pd.set_option('display.max.rows',1000)
print(emp[emp["Salary"] >= 149000].sort_values(by="Salary",ascending=False))
print(emp[emp["Salary"] >= 140000].sort_values(by=["Gender","Salary"],ascending=[False,True]))

