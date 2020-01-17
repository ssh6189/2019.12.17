import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#HTML형식의 파일로부터 테이블 읽기
file_path='./datas/sample.html'
tables=pd.read_html(file_path) 
print(len(tables))
 
for i in range(len(tables)):
   print("tables[%s]" % i)
   print(tables[i])

df = tables[1]
print(df)
df.set_index(['name'] , inplace=True)
print(df)
