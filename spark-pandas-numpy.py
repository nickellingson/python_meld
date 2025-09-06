# pandas
import pandas as pd

# read in csv data
pd_df = pd.read_csv("test.csv", delimiter= "\t")
print(pd_df)

# remove comma and make salary row number
pd_df["Salary"] = pd_df["Salary"].str.replace(",", "")
print(pd_df)
pd_df["Salary"] = pd.to_numeric(pd_df["Salary"])
print(pd_df)

# find agg
pd_df_agg = pd_df.groupby("Department").agg(
    avg_sal_dept = ("Salary", "mean"),
    person_count_dept = ("Name", "count")
)
print(pd_df_agg)

# numpy

import numpy as np

# --- read TSV with a header into a structured array ---
arr = np.genfromtxt(
    "test.csv",
    delimiter="\t",
    names=True,             # use header row as field names
    dtype=None,             # auto-dtype; gives structured array
    encoding="utf-8"
)

print(arr)
# Expect fields: Name (str), Department (str), Salary (str with commas)
names = arr["Name"]
depts = arr["Department"]

# Remove commas and convert to float
salaries_str = arr["Salary"].astype(str)
salaries_num = np.char.replace(salaries_str, ",", "").astype(float)

# --- group by Department ---
# Map each dept to a group id
uniq_depts, inv = np.unique(depts, return_inverse=True)
print(uniq_depts)
print(inv)
# Count per dept
counts = np.bincount(inv)

# Sum salaries per dept (weighted bincount)
sum_salaries = np.bincount(inv, weights=salaries_num)

# Mean per dept (handle divide-by-zero just in case)
avg_salaries = sum_salaries / np.where(counts == 0, 1, counts)

# Build a compact result as a structured array (or dict)
dept_agg = np.rec.fromarrays(
    [uniq_depts, avg_salaries, counts],
    names=("Department", "avg_sal_dept", "person_count_dept")
)

# Pretty print
for dep, avg, cnt in dept_agg:
    print(f"{dep:20s} avg_sal_dept={avg:.2f}  person_count_dept={int(cnt)}")


from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()
# Read TSV with header
df = (
    spark.read
         .option("header", True)
         .option("delimiter", "\t")
         .csv("test.csv")
)

# Remove commas from Salary and cast to double
df2 = (
    df.withColumn("Salary",
        F.regexp_replace(F.col("Salary"), ",", "").cast("double")
    )
)

# Group by Department: mean salary and count of Name
agg_df = (
    df2.groupBy("Department")
       .agg(
           F.avg("Salary").alias("avg_sal_dept"),
           F.count("Name").alias("person_count_dept")
       )
)

agg_df.show(truncate=False)