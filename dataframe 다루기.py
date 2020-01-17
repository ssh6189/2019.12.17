
# IPython.display은 IPython 셸 환경에서 dataframe을 테이블 형식으로 표현합니다.
import pandas as pd
import numpy as np
from IPython.display import display
my_2darray = np.array([[1,2,3], [4,5,6]])
display(pd.DataFrame(my_2darray))

dict_data = {'c0': [1,2,3], 'c1': [4,5,6], 'c2': [7,8,9], 'c3': [10,11,12], 'c4': [13,14,15]}
display( pd.DataFrame(dict_data))

df2 = pd.DataFrame([[25,'남' , '율도국'],[17, '여', '인당수']], index=['홍길동', '심청'], columns=['나이', '성별', '주소'])
display(df2)

exam_data= {'수학': [90,80,70],
                  '영어': [95,89,90],
                  '국어': [100,80,75],
                  '과학': [70,70,70]}
df = pd.DataFrame(exam_data, index=['영희', '철수', '삼식'])
print(df)

df2 = df[ : ]  # 새로운 DataFrame객체를 복제함
#print(id(df))
#print(id(df2))
result = df2.drop('삼식')  #행 인덱스(label)로 행 삭제한 새로운 데이터프레임 객체 생성 반환
print(df2)
print(result)

df2.drop('삼식', inplace=True)   #행 삭제한 새로운 데이터프레임 객체 반환대신 자기자신의 행 삭제
print(df2)

df2 = df[ : ]  # 새로운 DataFrame객체를 복제함
df2.drop('수학', axis=1,  inplace=True) 
print(df2)

#행 선택
student1 = df.loc['철수']   #label 을 사용해서 행을 선택
print(student1)
student2 = df.iloc[0]  #index 을 사용해서 행을 선택
print(student2)

students1 = df.loc[['철수', '삼식']]   #label 을 사용해서 2개 이상 행을 선택
print(students1)
students2 = df.iloc[[0,1]]  #index 을 사용해서 2개 이상 행을 선택
print(students2)

students3 = df.loc['철수':'삼식']   #행 인덱스 범위 지정,  행 선택, end label을 포함
print(students3)
students4 = df.iloc[0:2]  #행 인덱스 범위 지정,  행 선택 end index는 포함하지 않는다.
print(students4)


exam_data= {'이름' : ['영희', '철수', '삼식'],
                  '수학': [90,80,70],
                  '영어': [95,89,90],
                  '국어': [100,80,75],
                  '과학': [70,70,70]}
df = pd.DataFrame(exam_data)
print(df)



###데이터 프레임에서 열을 선택

print(df['수학'])
eng =df.영어
print(eng)
print(type(eng))   #Series

subjects = df[['수학', '국어']]
print(subjects)
print(type(subjects)) #2개 이상이면, 데이터 프레임

print(df)
df.set_index('이름', inplace = True)
print(df)

#철수의 수학과 과학점수를 출력(label 인덱스와 index)
print("\n")
cheolsu = df.loc['철수', ['수학', '과학']]
print(cheolsu)

print("\n")
cheolsu = df.iloc[1, [0, 3]]
print(cheolsu)

#철수의 국어와 과학점수를 출력(label 인덱스와 index)
print("\n")
cheolsu = df.loc['철수', ['국어', '과학']] #또는 '국어':'과학'
print(cheolsu)

#철수의 국어와 과학점수를 출력(label 인덱스와 index)
print("\n")
cheolsu = df.iloc[1, 2:]
print(cheolsu)

#컬럼에 데이터 단일값으로 일괄 변
print(df)
df['과학'] = 95
print(df)

#행 추가 - 동일한 값으로 추가됨
df.loc[3] = 0
print(df)

df.loc['동식'] = [70,80,90,100] 
print(df)

df.loc['행5'] = df.loc[3] #기존 행 복사
print(df)

#철수의 수학과학 점수를 50으로 변경

df.loc['철수', ['수학', '과학']] = [50, 50]
print(df)

df = pd.DataFrame(exam_data)
print(df)

#데이터 프레임에서 전치를 수행하려면, 메소드 활용
df = df.transpose()
print(df)

df = df.T
print(df)

#인덱스 재지정 : reindex()
dict_data = {'c0':[1, 2, 3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df2 = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])

print(df2)

new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
new_df = df2.reindex(new_index) #새로운 데이터 프레임 객체를 생성 반환('r3', 'r4'행의 데이터는 NA)
print(df2)
print(new_df)

new_df = df2.reindex(new_index, fill_value=0) #reindex로 발생된 NA를 0으로 채움
print(df2)
print(new_df)

new_df = df2.reset_index() #새로운 데이터프레임 객체를 생성 반환, 행 인덱스를 정수형으로 초기화
print(new_df)

new_df = df2.sort_index(ascending = False) #새로운 데이터프레임 객체를 생성 반환, 행 인덱스를 기준으로 내림차순 정렬
print(new_df)

new_df = df2.sort_values(by='c3', ascending = False )  # 새로운 데이터프레임 객체를 생성 반환 , 행 인덱스기준으로 내림차순 정렬, 어떤 인덱스를 기준으로?

#시리즈는 오류없이 라벨이 같은 애들끼리 연산을 해준다.

student1 = pd.Series({'국어':100, '영어':90, '수학':80})
percentage = student1/300
print(percentage)
print(type(percentage))

student1 = pd.Series({'국어':np.nan, '영어':90, '수학':80})
student2 = pd.Series({'영어':90, '수학':80})


print(student1)
print(student2)
print(student1+student2) #student1.add(student2)
division = student1/student2
print(division)

re_add = student1.add(student2, fill_value=0)
re_sub = student1.sub(student2, fill_value=0)
re_mul = student1.mul(student2, fill_value=0)
re_div = student1.div(student2, fill_value=0)

result = pd.DataFrame([re_add, re_sub, re_mul, re_div], index = ['덧셈','뺄셈', '곱셈', '나눗셈'])
