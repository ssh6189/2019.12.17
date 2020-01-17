import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#누락 데이터 찾기

df = sns.load_dataset('titanic')

nan_dec_cnt = df['deck'].value_counts(dropna=False)

print(nan_dec_cnt)

#데이터 프레임의 데이터 요소별로 NA체크 -isnull(), notnull()
print(df.head())
print(df.head().isnull())
print(df.head().notnull())

#누락 데이터 개수 구하기

print(df.head().isnull().sum(axis=0))

#누락 데이터 대체하기
