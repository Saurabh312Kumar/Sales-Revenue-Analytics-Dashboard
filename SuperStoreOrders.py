import pandas as pd
from sqlalchemy import create_engine

pd.set_option('display.width',None)
#pd.set_option('display.max_columns',None)
pd.set_option('display.max_colwidth',None)

df=pd.read_csv('SuperStoreOrders.csv')

print(df.head(3))


print(df.info())

print(df.describe())
print(df.isnull().sum()) #checking for null values
#there are no null values
#df=df.dropna() #if any null values were present, it would drop them


df.columns=df.columns.str.strip()
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")

#modifying columns:

print(df['order_date'].dtype,df['ship_date'].dtype)# checking the data type of date and ship date column
#changing the data type of date and ship date column
df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True)
df['ship_date']=pd.to_datetime(df['ship_date'],format='mixed', dayfirst=True)

df['sales'] = df['sales'].str.replace(',', '', regex=True)
df['sales_numeric'] = pd.to_numeric(df['sales'])



#adding columns
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['month_name'] = df['order_date'].dt.month_name()

print(df[['year','month','month_name']].head(3))

#connecting to mysql
username="root"
password="Admin123"
host="localhost"
port="3306"
database="SuperStoreOrders"

engine=create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
table_name="store"
df.to_sql(table_name,engine,if_exists="replace",index=False)
print(f"data successfully loaded into table:{table_name} in database:{database}")




