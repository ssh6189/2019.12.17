import pandas as pd

file_path = 'C:/Users/student/Desktop/datas/datas/df_sample.json'

df = pd.read_json(file_path)
print(df)
print(df.index)
print(df.columns)
