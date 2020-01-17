import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

plt.rc('font', family='Malgun Gothic')
    
a = pd.read_csv('C:/Users/student/Desktop/기온.csv', 'r', encoding='cp949')
b = pd.read_csv('C:/Users/student/Desktop/강수량.csv', 'r',  encoding='cp949')

sa = 100
ra = 0

i = 0
j = 0


print(a.iloc[7])

#2000년도 ~ 2018년도 서울 지역 최저 기온과 날짜

df1 = pd.DataFrame(a, columns = ['날짜', '지점', '평균기온', '최저기온(℃)', '최고기온(℃)'])
df2 = pd.DataFrame(b, columns = ['날짜', '지점', '강수량'])

c1 = a.loc[:, ['날짜', '지점', '평균기온', '최저기온(℃)', '최고기온(℃)']]
print(c1.head())
print(df1.head())

print(df1.min(df1.iloc[:,[3]]))
for i in range(len(df1)):
    
    mini = df1.loc[i,['최저기온(℃)']]

    if(mini[i]<sa):
        sa = i
    else:
        pass

print(df1.iloc[i])

print("\n")

#2000년도 ~ 2018년도 서울 지역 최대 강수량과 날짜
for j in range(len(df2)):
    
    maxi = df2.iloc[j,[2]]

    if(maxi[j]>ra):
        ra = j
    else:
        pass

print(df2.iloc[j])

#3번  서울지역의 2000년도~2018년도 날씨 데이터로부터 년도별 가장 높은 날의 기온과  년도별 가장 높은 날의 기온을
#변화를 쉽게 파악할 수 있도록  시각화하시오
