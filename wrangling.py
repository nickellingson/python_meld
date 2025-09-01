import pandas as pd

employees_df = pd.read_csv('./test.csv', delimiter="\t")
print(employees_df)

# Clean salary column
print(employees_df["Salary"])
employees_df["Salary"] = employees_df["Salary"].str.replace(",", "")
print(employees_df)
employees_df["Salary"] = pd.to_numeric(employees_df["Salary"])

print(employees_df.columns.tolist())

# Average salary for each department
avg_salary_df = employees_df.groupby("Department").agg(
    avg_salary_by_dept = ("Salary", "mean"),
    count_of_dept = ("Department", "count")
)
print(avg_salary_df)