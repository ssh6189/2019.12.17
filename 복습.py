numpy 라이브러리 제공해주는 다차원 배열 객체 - numpy.ndarray

ndarray 배열 객체 속성 - 크기 shape, 차원 ndim, 자료형 dtype, 요소개수 size

ndarray 배열 객체 생성 함수 np.array(), arange(), zeros, ones, full(), eye(), logspace(), linspace(), 생성후 배열 객체 초기화시 사용 empty()

ndarray 배열 객체의 데이터를 난수로 초기화해서 생성
np.random.normal()
np.random.rand()
np.random.randint()
np.random.random()

하나의 ndarray 배열 객체를 파일에 저장 - save(), npy확장자
하나 이상의 ndarray 배열 객체를 파일에 저장 - savz(), npz확장자
파일에 저장된 ndarray 배열 객체를 실행 환경으로 불러와서 메모리에 객체로 생성하려면, load()
csv, txt 파일에 저장된 텍스트(형식)을 실행환경으로 불러와서 메모리에 ndarray 배열 객체를 생성해 주는 함수 loadtxt()
ndarray 배열 객체를 텍스트(형식)파일에 저장 - savetxt()

ndarray 배열 객체의 연산 처리 방식 - 같은 위치의 요소 데이터끼리 연산, 벡터라이징연산
차원이 다른 ndarray 배열 객체와 ndarray배열 객체의 연산 처리 방식 - 벡터연산 + 브로드캐스팅

ndarray 객체와 스칼라값의 연산 - 벡터 연산(분배법칙)
ndarray 배열 객체의 데이터 요소 선택, 필러, 부분 집합 추출 - 인덱싱, 슬라이싱

1차원의 ndarray배열 객체[col_idx]
2차원의 ndarray 배열 객체 [row_idx, col_idx] -> [:,:]가능, [[선택한 행 1, 3, 5], col_idx]] - 팬시 인덱스
2차원의 ndarray 배열 객체 [조건, 조건]

인덱싱, 슬라이싱은 원본 ndarray 배열 객체의 뷰를 리턴한다.
bool을 리턴하는 인덱싱 방식은 새로운 array 배열 객체를 반환
원본 ndarray 배열 객체의 새로운 ndarray 배열 객체 반환(생성) copy()
단항 유니버셜 함수 : sqrt(), exp()....

이항 유니버셜 함수 : add(), substract(), modf()....

집합 함수 : sum(), mean(), ....axis = None, axis = 0(행), axis = 1(열)

None의 의미 : 2차원이라할지라도 1차원으로 만들어 집계함수로 만든다.

2차원 ndarray 배열 객체(Matrix, 행렬)의 행렬곱 - ndarray 배열 객체.dot(), @
2차원 ndarray 배열 객체(Matrix, 행렬)의 역행렬 - ndarray 배열 객체.solve()
2차원 ndarray 배열 객체(Matrix, 행렬)의 전치행렬 - ndarray 배열 객체.T
2차원 ndarray 배열 객체의 형태를 변경 - reshape()
2차원 ndarray 배열 객체의 형태를 변경 + 요소 추가, 삭제 - resize()
2차원 ndarray 배열 객체에 행 열 데이터 추가 - append()
2차원 ndarray 배열 객체에 행, 열 데이터를 특정 위치에 추가 - insert()
2차원 ndarray 배열 객체에 행, 열 데이터 삭제 - delete()

2차원 ndarray 배열 객체에 2차원 ndarray 배열 객체를 결합 - concatename(), vstack(), hstack()

2차원 ndarray 배열 객체를 분리 - split()

ndarray 배열 객체에 저장되는 데이터 요소는 모두 동일한 타입



pandas의 1차원 배열 객체 - Series

Series에는 저장되는 데이터 요소가 서로 다른타입이어야 한다.

Series의 속성 - index, values, index.name

Series의 인덱스 객체 타입 - RangeIndex

Series에 저장되는 데이터 요소 타입 - dtypes

Series의 인덱스를 변경하면서 label로 변경하려면, Series 객체.index.name = ["name1", "name2", "name3",....]

Series 저장되는 데이터 요소에 접근하기 위해서 사용하는 방법 - indexing, label 사용
