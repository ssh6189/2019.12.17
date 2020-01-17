import numpy as np
import pandas as pd
import openpyxl

#csv
exam_data= {'name' : ['A', 'B', 'C'],
                  'Math': [90,80,70],
                  'English': [95,89,90],
                  'Korea': [100,80,75],
                  'Science': [70,70,70]}

df = pd.DataFrame(exam_data)
df.set_index('name', inplace=True)
print(df)
df.to_csv('C:/Users/student/Desktop/datas/output/exam_sample.csv')

#json
df.to_json('C:/Users/student/Desktop/datas/output/exam_sample.json')

#Excel
df.to_excel('C:/Users/student/Desktop/datas/output/exam_sample.xlsx')


dict_data = {'c0': [1,2,3], 'c1': [4,5,6], 'c2': [7,8,9], 'c3': [10,11,12], 'c4': [13,14,15]}
df2 = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df2)

writer=pd.ExcelWriter("C:/Users/student/Desktop/datas/output/df_excelwriter.xlsx")
df.to_excel(writer, sheet_name="sheet1")
df2.to_excel(writer, sheet_name="sheet2")
writer.save()
