import pandas as pd
pd.set_option('display.max.columns',120)
pd.set_option('display.max.rows',100)
names=["Name","Gender","StartDate","LastOriginTime","Salary","Bonus","SrMgmt","Team"]
emp=pd.read_csv("C:\\Users\\Mahendra\\Downloads\\employees.csv",skiprows=1,names=names)
# print(emp)

df1=emp[['Name','Gender','Salary','Bonus','Team']]
print(df1)

# group_by_team=emp.groupby("Team").sum()
# group_by_team=emp.groupby("Team")
# group_by_team=emp.groupby("Team").agg(avg_salary=('Salary',))

# print(df1.groupby("Team").count())
# print(df1.groupby("Team").sum())

df_agg=df1.groupby(["Team","Gender"]).agg({'Salary':['mean','sum','min','max'],'Bonus':['mean','sum','min','max']})
# print(df1.groupby(["Team","Gender"]).agg( total_salary=('Salary', 'sum')))
print(df_agg["Salary"])
print(df_agg[("Salary","min")])
print("Type=",type(df_agg))
# print(df_agg.loc["0"])
# print(group_by_team.mean())
# emp.to_csv("C:\\Users\\Mahendra\\Downloads\\EMP.csv")

# print(df1.groupby('Team').describe())