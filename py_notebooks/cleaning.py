#importing main libraries
import pandas as pd
import datetime as dt
file_path="D:/Python/DataCleaning_project(1)/raw_data/amazon_sales_dataset.csv"
df=pd.read_csv(file_path,parse_dates=['order_date']) 
#checking nulls
print('nulls check: \n',df.isnull().sum())
print('*'*50)

#checking duplicates
print('duplicates sum: \n',df.duplicated().sum()) 
#removing duplicates
print('rows before cleaning:',len(df))
df=df.drop_duplicates()
print('duplicates dropped succesfully')
print('rows after cleaning:',len(df)) 

#check for inconsistent texts(str)
#print(df.info())
print('*'*50)
print('checking inconsistent str')
print('*'*50)
for col in df.select_dtypes(include='str'):
    print(df[col].unique())
    df[col]=df[col].str.strip().str.lower().str.replace('\n','').str.replace('\t','')

#check for impossible int
print('*'*50)
print('check for impossible int results')
print('*'*50)
def check_int(col):
    if col=='discount_percent':
        res=df[(df['discount_percent'] <0) | (df['discount_percent'] >100)]
    elif col=='quantity_sold' or col=='review_count':
        res=df[df[col] <0]
    else:
        res=df[df[col] <=0]
    print(col,'result -->',res.shape[0])

for col in df.select_dtypes(include=['int', 'float']) :
    check_int(col)

#check any errors in prices calculations
print('*'*50)
print('check any errors in prices calculations')
print('*'*50)
print(df[df['price'] <df['discounted_price']]) 
correct_calc=0
false_calc=0
for price,disc_perc,disc_price in zip(df['price'],df['discount_percent'],df['discounted_price']) :
    if abs(price - (price * (disc_perc/100)) - disc_price) > 0.01 :
        false_calc+=1
    else :
        correct_calc +=1
print('correct rows :',correct_calc)
print('wrong rows :',false_calc)

right_calc=0
wrong_calc=0
for q_sold,disc_price,total_rev in zip(df['quantity_sold'],df['discounted_price'],df['total_revenue']) :
    if abs(q_sold * disc_price - total_rev) > 0.01 :
        wrong_calc +=1
    else :
        right_calc +=1
print('correct rows :',right_calc)
print('wrong rows :',wrong_calc) 

# rating range
print('*'*50)
print('rating range check')
print('*'*50)
print(df['rating'].between(1, 5).value_counts())

#checking order dates
print('*'*50)
print('checking order dates')
print('*'*50)
print((df['order_date'] > dt.datetime.today()).sum())
df = df[df['order_date'] <= pd.Timestamp.today()]

#saving file
clean_path='D:/Python/DataCleaning_project(1)/cleaned_data/final_amazon_sales_dataset_clean.csv'
df.to_csv(clean_path)