
import  seaborn as sns
import pandas as pd

file_path = 'C:/Users/student/Desktop/datas/datas/read_csv_sample.csv'

df = pd.read_csv(file_path)
print(df)
print(type(df))

df2 = pd.read_csv(file_path, header = None)
print(df2)
print(type(df2))

df3 = pd.read_csv(file_path, index_col= None)
print(df3)
print(type(df3))

df4 = pd.read_csv(file_path, index_col= 'c0')
print(df4)
print(type(df4))

file_path = 'C:/Users/student/Desktop/datas/datas/남북한발전전력량.xlsx'
df = pd.read_excel(file_path)
print(df)
print(type(df))
print(df.dtypes)

df1 = pd.read_excel(file_path, header = None)
print(df1)
print(type(df1))



file_path='./datas/남북한발전전력량.xlsx'
df=pd.read_excel(file_path)
print(df)
print(type(df))
print(df.dtypes)

df1=pd.read_excel(file_path, header=None)
print(df1)
print(type(df1))
 
