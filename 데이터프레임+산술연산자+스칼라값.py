#데이터프레임+ 산술연산자+스칼라값
import  seaborn as sns
titanic = sns.load_dataset('titanic')

df= titanic.loc[ : , ['age', 'fare']]
print(df.head())
print(type(df))
addition = df+10
print(addition .head())
print(type(addition))

subtraction= addition - df
print(subtraction .head())
print(subtraction .tail())
print(type(subtraction))
