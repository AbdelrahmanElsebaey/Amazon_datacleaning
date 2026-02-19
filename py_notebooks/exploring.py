import pandas as pd
raw="D:/Python/DataCleaning_project(1)/raw_data/amazon_sales_dataset.csv"
df=pd.read_csv(raw)
print(df.head()) #explore first 5 rows
print(df.columns) #explore column names
print(df.describe()) #for some data stats
df.info()