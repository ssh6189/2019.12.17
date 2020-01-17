#데이터 프레임에 함수적용

frame = pd.DataFrame(np.random.randn(4,3), columns = list('bde'),
                     index = ['Utah', 'Ohio', 'Texas', 'Oregon'])

frame
np.abs(frame)

print(frame)

def f(x):
    return pd.Series([x.min(), x.max()], index=['min','max'])

frame.apply(f)

print(frame)

format = lambda x:"%.2f"%x
frame.applymap(format)

print(frame)
