import pandas as pd
# pd.set_option('display.max.rows',1000)
# pd.set_option('display.max.columns',10)
names=["Name","Gender","StartDate","LastOriginTime","Salary","Bonus","SrMgmt","Team"]
emp=pd.read_csv("C:\\Users\\Mahendra\\Downloads\\employees.csv",skiprows=1,names=names)

# print(emp)
print("######## DataFrame Info ########")
print(emp.info())
print("######## DataFrame Shape ########")
print(emp.shape)
print("######## DataFrame Head & Tail ########")
print(emp.head(1))
print(emp.tail(1))
print("######## Select Columns Data ########")
print(emp["Name"])
print("######## Select Columns Data loc ########")
print(emp.loc[1])