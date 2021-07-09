# Pandas - 교재 237쪽
    - series, DataFrame등의 자료구조를 활용한 데이터분석 기능을 제공해주는 라이브러리
    - 라이브러리 구성
        - 여러종류의 클래스와 다양한 함수로 구성
        - 시리즈와 데이터 프레임의 자료 구조 제공
        - 시리즈(1차원 배열) 데이터프레임(2차원 배열)
    -anaconda에 기본으로 설치되어 있음

#### 판다스의 목적
    - 서로 다른 유형의 데이터를 공통된 포맷으로 정리하는 것
    - 행과 열로 이루어진 2차원 데이터프레임을 처리 할 수 있는 함수제공 목적
    - 실무 사용 형태 : 데이터 프레임


### 구조적 데이터 생성하기 - Series/DataFrame

#### Series(교재 pp 237~240)
  - pandas의 기본 객체 중 하나
  - numpy의 ndarray를 기반으로 인덱싱을 기능을 추가하여 1차원 배열을 나타냄
  - index를 지정하지 않을 시, 기본적으로 ndarray와 같이 0-based 인덱스 생성
  - 지정할 경우 명시적으로 지정된 index를 사용
  - !!!!!같은 타입의 0개 이상의 데이터를 가질 수 있음!!!!!(가져야함)


1. 자료구조: 시리즈
    - 데이터가 순차적으로 나열된 1차원 배열 형태
    - 인덱스(index)와 데이터 값(value)이 일대일로 대을
    - 딕셔너리와 비슷한 구조 : {key(index):value}
    
    
2. 시리즈의 인덱스
    - 데이터 값의 위치를 나타내는 이름표 역할
    
    
3. 시리즈 생성 : 판다스 내장함수인 Series()이용
    - 리스트로 시리즈 만들기
    - 딕셔너리로 시리즈 만들기
    - 튜플로 시리즈 만들기



```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all" #(기본값은 'last_expr')
```


```python
# pandas package import
# 대부분의 코드에서 pandas as ps 로 import 한다
import pandas as pd
#numpy package import
import numpy as np
```

#### Series 생성하기

- data로만 생성하기
    - index는 명시하지 않으면 0부터 자동 생성된다


```python
#문법 : 변수 = pd.series()
blank_s = pd.Series()
blank_s #dtype: float64
```

    <ipython-input-6-823019da31c4>:2: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
      blank_s = pd.Series()
    




    Series([], dtype: float64)




```python
s0 = pd.Series(1) #인덱스 명시하지 않고 데이터 1개로 생성 - 인덱스는 0부터 시작하는 0-based 인덱스 생성
s0
```




    0    1
    dtype: int64




```python
s0[0] #0번 인덱스 원소값 접근
```




    1




```python
# 2개 이상의 원소 값을 갖는 시리즈를 생성할 경우 - list, tuple, dict 등을 사용해야 한다.
s1 = pd.Series([1,2])
s1
```




    0    1
    1    2
    dtype: int64




```python
# 서로 다른 data type의 원소를 갖는 list를 활둉한 series
s1_1 = pd.Series([1,2.0,3.5]) #float64 형태의 series
s1_1
```




    0    1.0
    1    2.0
    2    3.5
    dtype: float64




```python
s1_2 = pd.Series(['a',1,5.0]) #dtype: object : 숫자와 문자가 혼용되면 문자 형태로 series 생성
s1_2
```




    0      a
    1      1
    2    5.0
    dtype: object




```python
#tuple로 series 만들기 - list와 동일한 방법
s1_3 = pd.Series((1,2,3))
s1_3
```




    0    1
    1    2
    2    3
    dtype: int64



- 범위를 series의 value 생성하는데 사용하기 - range()/np.arange()


```python
s = pd.Series(range(10,14))
s
```




    0    10
    1    11
    2    12
    3    13
    dtype: int64




```python
s = pd.Series(np.arange(200))
s
```




    0        0
    1        1
    2        2
    3        3
    4        4
          ... 
    195    195
    196    196
    197    197
    198    198
    199    199
    Length: 200, dtype: int32



- 결측값을 포함해서 series를 만들기
    - 결측값은 NaN : numpy라는 모듈의 nan 속성을 통해서 생성 가능 -> np.nan


```python
s = pd.Series([1,2,3,np.nan,6,8]) #결측값이 포함되면 NaN은 float형으로 처리된다.
s
```




    0    1.0
    1    2.0
    2    3.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64



- index를 명시해서 series 만들기
    - 숫자 index지정/문자 index지정 가능
    - 변수 = pd.Series([값1,값2,...,값n],index=[index1,index2,index3,...,n])


```python
#index 명시해서 series 생성(수치 index)
s = pd.Series([10,20,30],index=[1,2,3])
s
```




    1    10
    2    20
    3    30
    dtype: int64




```python
s.index
```




    Int64Index([1, 2, 3], dtype='int64')




```python
#index 명시해서 series 생성(문자 index)
s = pd.Series([10,20,30],index=['홍길동','이몽룡','성춘향'])
s
```




    홍길동    10
    이몽룡    20
    성춘향    30
    dtype: int64



- index 활용 : 
    - series의 index는 index속성으로 접근

- series.index.name 속성
    - series의 index에 이름을 붙일 수 있음


```python
s
```




    홍길동    10
    이몽룡    20
    성춘향    30
    dtype: int64




```python
s.index.name = '이름'
s
```




    이름
    홍길동    10
    이몽룡    20
    성춘향    30
    dtype: int64



### 예제 df 생성


```python
s= pd.Series([9904312,3448737,289045,2466052],
            index=["서울","부산","인천","대구"]) #dtype='object' datatype = '문자열객체'
s.index

```




    Index(['서울', '부산', '인천', '대구'], dtype='object')




```python
s.index.name= '도시'
s
```




    도시
    서울    9904312
    부산    3448737
    인천     289045
    대구    2466052
    dtype: int64



series의 실제 값 추출 => series.values 속성 사용


```python
s.values #array 구조로 반환
```




    array([9904312, 3448737,  289045, 2466052], dtype=int64)



- series.name 속성
    - seires data(values)에 이름을 붙일 수 있다
    - name 속성은 값의 의미 전달에 사용


```python
s.name = '인구'
s
```




    도시
    서울    9904312
    부산    3448737
    인천     289045
    대구    2466052
    Name: 인구, dtype: int64



##### 딕셔너리로 시리즈 만들기
- Series({key:value,key1:value1....})
- 인덱스 -> key
- 값 -> value
- key가 index로 처리 되므로 명시적으로 index를 설정하게 된다


```python
scores = {'홍길동':96,'이몽룡':100,'성춘향':88}
s = pd.Series(scores)
s
```




    홍길동     96
    이몽룡    100
    성춘향     88
    dtype: int64




```python
city = {'서울' : 9639399, '부산':3392939,'인천':2639403,'대전':1490303}
s = pd.Series(city)
s
```




    서울    9639399
    부산    3392939
    인천    2639403
    대전    1490303
    dtype: int64



- 딕셔너리의 원소는 순서를 갖지 않는다.
    - 딕셔너리로 생성된 시리즈의 원소도 순서가 보장되지 않는다.
    - 만약 순서를 보장하고 싶으면 인덱스를 리스트로 지정해야 한다.



```python
s2 = pd.Series(city,index=['부산','인천','서울','대전'])
s2                   
```




    부산    3392939
    인천    2639403
    서울    9639399
    대전    1490303
    dtype: int64



### 인덱싱 :
    - data에서 특정한 data를 추출하는 것

### series의 인덱싱 종류

1. 정수형 위치 인덱스(integer position)
2. 인덱스 이름(index name) 또는  인덱스 라벨(index label)

    - 인덱스 별도 지정하지 않으면 0부터 시작하는 정수형 인덱스가 지정됨

#### 원소 접근
    - 정수형 index : 숫자 s[n]
    - 문자형 index : 숫자 s['인천']



```python
print(s.index)
s
```

    Index(['서울', '부산', '인천', '대전'], dtype='object')
    




    서울    9639399
    부산    3392939
    인천    2639403
    대전    1490303
    dtype: int64




```python
# 위치 index
s[0] #서울의 값을 반환
```




    9639399




```python
# 라벨 index
s['서울']
```




    9639399




```python
### 확인 예제
s_1 = pd.Series([1,2,3],index=[1,2,3])
s_1
```




    1    1
    2    2
    3    3
    dtype: int64




```python
s_1.index
# s_1[0] #index의 종류가 정수형이면 위치 index 사용이 불가능하다.
```




    Int64Index([1, 2, 3], dtype='int64')




```python
# 한줄에 위치 index, 문자 index를 동시에 접근
s
s[3],s['대전'] #tuple생성
```




    서울    9639399
    부산    3392939
    인천    2639403
    대전    1490303
    dtype: int64






    (1490303, 1490303)



#### list이용 indexing
    - 자료의 순서를 바꿔 반환하거나, 특정 자료 여러개를 선택할 때 사용
    - 시리즈명[[index1,index2,...]]


```python
s
s[[0,3,1]]
```




    서울    9639399
    부산    3392939
    인천    2639403
    대전    1490303
    dtype: int64






    서울    9639399
    대전    1490303
    부산    3392939
    dtype: int64




```python
s[['서울','인천']]
```




    서울    9639399
    인천    2639403
    dtype: int64



##### 시리즈 슬라이싱을 이용한 인덱싱
- 정수형 위치 인덱스를 사용한 슬라이싱
    - 시리즈[start:stop+1]
    
    
- 문자(라벨)인덱스 이용 슬라이싱
    - 시리즈['시작라벨':'끝라벨']  : 표시된 라벨 범위 모두 추출



```python
s
```




    서울    9639399
    부산    3392939
    인천    2639403
    대전    1490303
    dtype: int64




```python
# 위치 index 스라이싱
s[1:3] #1~2 index 출력
```




    부산    3392939
    인천    2639403
    dtype: int64




```python
# 문자 index를 이용한 슬라이싱
s['부산':'대전']
```




    부산    3392939
    인천    2639403
    대전    1490303
    dtype: int64




```python
### 슬라이싱 예제 - 명시적으로 설정한 정수 index를 슬라이싱하면 위치 슬라이싱이 적용
s_test = pd.Series([1,2,3,4],index=[1,3,5,7])
s_test
```




    1    1
    3    2
    5    3
    7    4
    dtype: int64




```python
s_test[1:5]
```




    3    2
    5    3
    7    4
    dtype: int64




```python
### 문자 index의 경우에는 .를 이용해서 접근할 수 있음
s
```




    서울    9639399
    부산    3392939
    인천    2639403
    대전    1490303
    dtype: int64




```python
s.서울
```




    9639399




```python
s_test
```




    1    1
    3    2
    5    3
    7    4
    dtype: int64




```python
s_test.1 # .연산자를 이용한 원소 접근은 문자 index만 가능함
```


      File "<ipython-input-74-874e2ee8deb3>", line 1
        s_test.1
              ^
    SyntaxError: invalid syntax
    


#### indexing을 통한 data 업데이느
    -시리즈명[index] = data값


```python
s
```




    서울    9639399
    부산    3392939
    인천    2639403
    대전    1490303
    dtype: int64




```python
s['서울'] = 10000000 #dict와 동일한 방법
s
```




    서울    10000000
    부산     3392939
    인천     2639403
    대전     1490303
    dtype: int64



#### index 재사용 가능


```python
s.index
s1 = pd.Series(np.arange(4),s.index)
s1
```




    Index(['서울', '부산', '인천', '대전'], dtype='object')






    서울    0
    부산    1
    인천    2
    대전    3
    dtype: int32



## series 연산


```python
# 예제 series
s
# 서울    10000000
# 부산     3392939
# 인천     2639403
# 대전     1490303
# dtype: int64
```




    서울    10000000
    부산     3392939
    인천     2639403
    대전     1490303
    dtype: int64



##### 벡터화 연산
- numpy 배열처럼 pandas의 시리즈도 벡터화 연산 가능 
- 벡터화 연산이란 집합적 자료형의 원소 각각을 독립적으로 계산을 진행하는 방법
    - 단, 연산은 시리즈의 값에만 적용되며 인덱스 값은 변경 불가



```python
pd.Series([1,2,3]) + 4
```




    0    5
    1    6
    2    7
    dtype: int64




```python
#s 시리지의 값은 1/1000000 변환
s/1000000
```




    서울    10.000000
    부산     3.392939
    인천     2.639403
    대전     1.490303
    dtype: float64




```python
# 벡터화 인덱싱 - 인덱싱에 조건식을 활용할 수 있다.
# 시리즈 s의 원소값 중 2500000 보다 크고 5000000 보다 작은 원소를 추출
# 시리즈명[조건식] - 각 원소의 값 모두를 각각 조건식으로 확인해서 결과가 True인 원소만 추출

s[(s>250e4) & (s<500e4)]
```




    부산    3392939
    인천    2639403
    dtype: int64



#### **Boolean selection**
  - boolean Series가 []와 함께 사용되면 True 값에 해당하는 값만 새로 반환되는 Series객체에 포함됨
  - 다중조건의 경우, &(and), |(or)를 사용하여 연결 가능



```python
s0 = pd.Series(np.arange(10), np.arange(10)+1)
s0

```




    1     0
    2     1
    3     2
    4     3
    5     4
    6     5
    7     6
    8     7
    9     8
    10    9
    dtype: int32




```python
s0[s0>6]
```




    8     7
    9     8
    10    9
    dtype: int32




```python
# s0 시리즈의 원소 값 중 짝수 원소 값을 추출하시오
s0[s0%2==0]
```




    1    0
    3    2
    5    4
    7    6
    9    8
    dtype: int32




```python
s0[s0.index > 5] #s0 index값이 5를 초과흐는 원소 출력
```




    6     5
    7     6
    8     7
    9     8
    10    9
    dtype: int32




```python
(s0 >= 7).sum() #True의 개수가 몇개인지 반환
```




    3




```python
s0[s0>=7].sum() #출력되는 원소의 값을 모두 더해 반환
```




    24



s0 = pd.Series(np.arange(10), np.arange(10)+1)
s0
s0 > 5
s0[s0>5]
# s0 시리즈의 원소 값 중 짝수 원소 값을 추출하시오
s0 % 2 == 0
s0[s0 % 2 == 0]
s0.index  > 5 # s0의 인덱스 값을 추출해서 벡터화 연산 진행
s0[s0.index > 5] # s0인덱스값이 5를 초과하는 원소 출력
(s0 >= 7).sum() # 각 원소에 대하여 조건식의 결과값이  True인 원소의 개 수
s0[s0>=7]
s0[s0>=7].sum() # 각 원소에 대해 대입한 조건식의 결과값이 True인 원소들의 합


- 두 시리즈 간의 연산


```python
num_s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
num_s2 = pd.Series([5,6,7,8],index=['b','c','d','a'])
num_s1
num_s2
```




    a    1
    b    2
    c    3
    d    4
    dtype: int64






    b    5
    c    6
    d    7
    a    8
    dtype: int64




```python
num_s1 + num_s2 #시리즈간의연산은 같은 인덱스를 찾아 진행
```




    a     9
    b     7
    c     9
    d    11
    dtype: int64




```python
num_s3 = pd.Series([1,2,3,4],index=['e','b','f','g'])
num_s4 = pd.Series([5,6,7,8],index=['b','c','d','a'])
num_s3
num_s4
```




    e    1
    b    2
    f    3
    g    4
    dtype: int64






    b    5
    c    6
    d    7
    a    8
    dtype: int64




```python
num_s3 + num_s4 #동일 인덱스를 찾지 못하면 결측값을 출력
```




    a    NaN
    b    7.0
    c    NaN
    d    NaN
    e    NaN
    f    NaN
    g    NaN
    dtype: float64




```python
num_s4.values - num_s3.values
# values 속성을 사용하면 시리즈의 형태가 사라지므로 동일한 위치 원소들끼리 연산 진행
# 시리즈의 values는 array 형태를 반환
```




    array([4, 4, 4, 4], dtype=int64)



##### 딕셔너리 와 시리즈의 관계
- 시리즈 객체는 라벨(문자)에 의해 인덱싱이 가능
- 실질적으로는 라벨을 key로 가지는 딕셔너리 형과 같다고 볼 수 있음
- 딕셔너리에서 제공하는 대부분의 연산자 사용 가능
    - in 연산자 : T/F
    - for 루프를 통해 각 원소의 key와 value에 접근 할수 있다.


- in연산자 / for 반복문


```python
s
```




    서울    10000000
    부산     3392939
    인천     2639403
    대전     1490303
    dtype: int64




```python
# s시리즈의 인덱스가 서울인 원소가 시리즈에 있는지 확인
'서울' in s #True 
```




    True




```python
'대구' not in s #True
```




    True




```python
#dict의 items() 함수를 시리즈에서도 사용 가능
s.items()
list(s.items())
```




    <zip at 0x1d13403d380>






    [('서울', 10000000), ('부산', 3392939), ('인천', 2639403), ('대전', 1490303)]




```python
#반복문을 활용해서 시리즈의 각 원소를 출력하는 코드
for i,j in s.items():
    print('%s=%d' % (i,j))
```

    서울=10000000
    부산=3392939
    인천=2639403
    대전=1490303
    

#### 시리즈 데이터의 갱신/추가/삭제
- 인덱싱을 사용하면 딕셔너리 처럼 갱신 추가


```python
s
```




    서울    10000000
    부산     3392939
    인천     2639403
    대전     1490303
    dtype: int64




```python
# s시리즈의 부산의 인구 값을 4630000으로 갱신
s['부산'] = 4630000
s
```




    서울    10000000
    부산     4630000
    인천     2639403
    대전     1490303
    dtype: int64




```python
#시리즈에 새로운 대구 데이터를 추가
s['대구'] = 5000000
s
```




    서울    10000000
    부산     4630000
    인천     2639403
    대전     1490303
    대구     5000000
    dtype: int64




```python
#시리즈에 데이터 삭제 : del 명령 사용
del s['대전']
s

```




    서울    10000000
    부산     4630000
    인천     2639403
    대구     5000000
    dtype: int64



### Series Function

#### **Series size, shape, unique, count, value_counts 함수**
 - size(속성): 개수 반환
 - shape(속성) : 튜플형태로 shape반환
 - unique: 유일한 값만 ndarray로 반환
 - count : NaN을 제외한 개수를 반환
 - mean: NaN을 제외한 평균 
 - value_counts: NaN을 제외하고 각 값들의 빈도를 반환



```python
s1 = pd.Series([1, 1, 2, 1, 2, 2, 2, 1, 1, 3, 3, 4, 5, 5, 7, np.NaN])
s1
```




    0     1.0
    1     1.0
    2     2.0
    3     1.0
    4     2.0
    5     2.0
    6     2.0
    7     1.0
    8     1.0
    9     3.0
    10    3.0
    11    4.0
    12    5.0
    13    5.0
    14    7.0
    15    NaN
    dtype: float64




```python
len(s1) #NaN값을 포함한 개수
```




    16




```python
s1.size #NaN값을 포함한 개수
```




    16




```python
s1.shape #차원을 표현하기때문에 tuple형태로 출력
#16행이 존재하고 열은 존재하지 않는다
```




    (16,)




```python
s1.unique() #중복데이터를 제거하고 원소값을 출력
```




    array([ 1.,  2.,  3.,  4.,  5.,  7., nan])




```python
s1.count() #NaN값을 제거한 원소의 개수를 출력
```




    15




```python
a = np.array([2,2,2,2,2,np.NaN]) #결측치 포함
b = pd.Series(a) #
a.mean() #np의 array를 평균 계산 - NaN이 포함되면 계산 불가(NaN반환)
b.mean() # 기본 nan 값을 제외시키고 계산하도록 설정
```




    nan






    2.0




```python
s1.mean()
```




    2.6666666666666665




```python
s1.value_counts() #각 원소들을 같은 값끼리 그룹을 만들고 개수를 세서 반환
```




    1.0    5
    2.0    4
    3.0    2
    5.0    2
    7.0    1
    4.0    1
    dtype: int64




```python

```


```python

```


```python

```
