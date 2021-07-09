```python
#설정변경코드
#변수 명이 두번 이상 출력되어도 모두 콘솔에서 보여줄 것
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"

# InteractiveShell.ast_node_interactivity : 'all' | 'last' | 'last_expr' | 'none' (기본값은 'last_expr')

```


```python
import pandas as pd
import numpy as np
```

### pandas 데이터 처리 및 변환 관련 함수

### 데이터 개수 세기
- 가장 간단한 분석은 개수를 세는 것임
- count() 함수 사용
    - NaN 값은 세지 않는다


```python
# 시리지으세 개수 세기
s = pd.Series(range(10))
s[3] = np.nan
s
```




    0    0.0
    1    1.0
    2    2.0
    3    NaN
    4    4.0
    5    5.0
    6    6.0
    7    7.0
    8    8.0
    9    9.0
    dtype: float64




```python
s.count()
```




    9



### 난수
- 난수 : seed(값) 라는 함수 사용 가능
- seed의 의미 : 난수 알고리즘에서 사용하는 기본값으로 시드값이 같으면 동일한 난수가 발생함
    


```python
np.random.seed(2) #난수값을 고정하기 위해 사용 난수 발생 함수와 반드시 함께 사용해야함
np.random.randint(5,size=4)
```




    array([0, 0, 3, 2])




```python
np.random.seed(1)
np.random.randint(5,size=4) #seed() 함수가 같이 실행되지 않기 때문에 실행시마다 다른 결과가 반환
```




    array([3, 4, 0, 1])




```python
#예제 데이터 프레임 생성
# 데이터 0-4범위의 난수 발생, 4행4열, 실수형데이터로 생성
# np.random.seed(3)
# df=pd.DataFrame(np.random.randint(5,size=(4,4)),dtype=float)
# display(df)
np.random.seed(3)
df1=pd.DataFrame(np.random.randint(5,size=(4,4))) #기본 정수
df1
df1.iloc[2,3] =np.nan
df1

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df의 count()는 각 열에 대한 연산을 진행 - 각 열의 유효한 원소의 개수를 반환
df1.count() 
```




    0    4
    1    4
    2    4
    3    3
    dtype: int64



##### count() 사용 예제 : (titanic data)

- 타이타닉 승객 데이터 사용
    - seaborn 패키지 내에 data로 존재
    - 데이터셋 읽어오기 : 패키지명.load_dataset("data명")



```python
import seaborn as sns  #그래프 패키지

titanic = sns.load_dataset('titanic')
titanic
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>0</td>
      <td>2</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>13.0000</td>
      <td>S</td>
      <td>Second</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>887</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>30.0000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>B</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>888</th>
      <td>0</td>
      <td>3</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>23.4500</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>889</th>
      <td>1</td>
      <td>1</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>30.0000</td>
      <td>C</td>
      <td>First</td>
      <td>man</td>
      <td>True</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>890</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.7500</td>
      <td>Q</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Queenstown</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 15 columns</p>
</div>




```python
#titanic df의 각 열의 원소 개수 산출 - count()함수 이용
titanic.shape
titanic.count() #시리즈 반환 - 전체 행에 대해 값 차이가 나는 열은 결측치를 포함하고 있다는 의미
```




    (891, 15)






    survived       891
    pclass         891
    sex            891
    age            714
    sibsp          891
    parch          891
    fare           891
    embarked       889
    class          891
    who            891
    adult_male     891
    deck           203
    embark_town    889
    alive          891
    alone          891
    dtype: int64



###  카테고리 값 세기
- 시리즈의 값이 정수,문자열 등 카테고리 값인 경우에
- 시리즈.value_counts()메서드를 사용해 각각의 값이 나온 횟수를 셀 수 있음
- 파라미터 normalize=True 를 사용하면 각 값 및 범주형 데이터의 비율을 계산
    - 시리즈.value_counts(normalize=True)



```python
np.random.seed(1)
s2 = pd.Series(np.random.randint(6,size=100)) #6까지의 정수 중 100개를 랜덤하게 
s2.tail()
len(s2)

```




    95    4
    96    5
    97    2
    98    4
    99    3
    dtype: int32






    100






    1    22
    0    18
    4    17
    5    16
    3    14
    2    13
    dtype: int64




```python
s2.value_counts()
```




    1    22
    0    18
    4    17
    5    16
    3    14
    2    13
    dtype: int64



##### 범주형 데이터에 value_counts() 함수 적용
- 범주형 데이터 : 관측 결과가 몇개의 범주 또는 항목의 형태로 나타나는 자료
    - ex. 성별(남,여), 선호도(좋다, 보통, 싫다), 혈액형(A,B,O,AB) 등



```python
titanic.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# alive 열 : 생존여부 yes/no로 표시되어 있음
titanic['alive'].dtype
titanic['alive'].value_counts()
```




    dtype('O')






    no     549
    yes    342
    Name: alive, dtype: int64




```python
#생존/사망자 비율 계산
titanic['alive'].value_counts(normalize = True) * 100
```




    no     61.616162
    yes    38.383838
    Name: alive, dtype: float64



##### df에 value_counts() 함수 사용
- 행을 하나의 value로 정의, 동일한 행이 몇번 나타났는지를 반환해줌
- 행 데이터의 경우가 인덱스로 설정됨, 개수된 값이 value로 표시되는 Series 반환


```python
# 예제 df
df = pd.DataFrame({'num_legs': [2, 4, 4, 6],
                   'num_wings': [2, 0, 0, 0]},
                  index=['falcon', 'dog', 'cat', 'ant'])
df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>cat</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>ant</th>
      <td>6</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.value_counts()
df.value_counts().index
```




    num_legs  num_wings
    4         0            2
    2         2            1
    6         0            1
    dtype: int64






    MultiIndex([(4, 0),
                (2, 2),
                (6, 0)],
               names=['num_legs', 'num_wings'])




```python
#예제
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.value_counts() #행 원소로 NaN값이 있는 필드는 제외하고 출력
```




    0  1  2  3  
    0  0  0  3.0    1
    2  0  1  3.0    1
          4  4.0    1
    dtype: int64




```python
df1.value_counts().shape
df1.value_counts().sort_index().index
```




    (3,)






    MultiIndex([(0, 0, 0, 3.0),
                (2, 0, 1, 3.0),
                (2, 0, 4, 4.0)],
               names=[0, 1, 2, 3])



### data정렬 - 정렬 함수 사용
- sort_index() : index를 기준으로 정렬한다
- sort_value() : data값을 기준으로 정렬

#### 시리즈 정렬


```python
#예제 시리즈
s2
```




    0     5
    1     3
    2     4
    3     0
    4     1
         ..
    95    4
    96    5
    97    2
    98    4
    99    3
    Length: 100, dtype: int32



#### 시리즈 정렬(시리즈.sort_index())
    -ascending=True/False : 오름차순/내림차순
    -생략하면 오름차순


```python
s2.value_counts() #반환 값을 기준으로 정렬된 시리즈
s2.value_counts().sort_index() #index 기준 정렬 : 오름차순
s2.value_counts().sort_index(ascending=False) #index기준 정렬 : 내림차순

```




    1    22
    0    18
    4    17
    5    16
    3    14
    2    13
    dtype: int64






    0    18
    1    22
    2    13
    3    14
    4    17
    5    16
    dtype: int64






    5    16
    4    17
    3    14
    2    13
    1    22
    0    18
    dtype: int64




```python
s2.value_counts().sort_values() #값을 기준으로 정렬 :오름차순
s2.value_counts().sort_values(ascending=False) # 값을 기준으로 정렬 : 내림차순
```




    2    13
    3    14
    5    16
    4    17
    0    18
    1    22
    dtype: int64






    1    22
    0    18
    4    17
    5    16
    3    14
    2    13
    dtype: int64




```python
s2.sort_values()
```




    57    0
    38    0
    39    0
    85    0
    28    0
         ..
    71    5
    40    5
    46    5
    11    5
    0     5
    Length: 100, dtype: int32



### 데이터 프레임 정렬

- df.sort_values() : 특정열 값 기준 정렬
    - 데이터프레임은 2차원 배열과 동일하기 때문에
        - 정렬시 기준열을 줘야 한다. by 인수 사용 : 생략 불가
        - by = 기준열, by=[기준열1,기준열2]
    - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)
- df.sort_index() : DF의 INDEX 기준 정렬
    - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)



```python
# 예제 df1
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.sort_values() #기준열이 없어 정렬 불가
```


      File "<ipython-input-110-206531d0d0d5>", line 1
        df1.sort_values(by'1')
                          ^
    SyntaxError: invalid syntax
    



```python
df1.sort_values(by = 0,ascending=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.sort_values(by = 0,ascending=False) #0번열 기준 내림차순 정렬
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.sort_values(by = [0,1,2],ascending=True) #0번열을 기준으로 정렬 0열 값이 동일할 때 1열 값 기준으로 재정렬 함 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#df
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>cat</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>ant</th>
      <td>6</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



- df의 index를 기준으로 정렬


```python
df.sort_index()
df.sort_index(ascending = False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ant</th>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>cat</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>cat</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>ant</th>
      <td>6</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



# 데이터 프레임 조작 함수 정리


### 행/열 합계
- df.sum() 함수 사용
- 행과 열의 합계를 구할때는 sum(axis=0/1) - axis는 0이 기본


- 각 열의 합계를 구할때는 sum(axis=0)
- 각 행의 합계를 구할때는 sum(axis=1)



```python
# 예제 DF 생성
#4행 8열의 데이터프레임 작성, 난수를 발생시키고
#0-9범위에서 매번 같은 난수 발생되어 반환되도록 설정
np.random.seed(1)
df2=pd.DataFrame(np.random.randint(10,size=(4,8)))
df2

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
#df2의 각 열의 합계 = sum(axis = 0)
df2.sum(axis=0) #시리즈 반환
df2.sum() #axis값 생략시 0과 같다 => 기본값 0
```




    0    24
    1    33
    2    25
    3    24
    4    15
    5    10
    6     5
    7    16
    dtype: int64






    0    24
    1    33
    2    25
    3    24
    4    15
    5    10
    6     5
    7    16
    dtype: int64




```python
#df2의 각 행의 합계
df2.sum(axis = 1 ) #각 행의 합계 출력
```




    0    35
    1    34
    2    41
    3    42
    dtype: int64



- 데이터 프레임 기본 함수 확인


```python
#평균/최대/최소 값을 구하는 함수 : 각 열이나 행 단위로 연산을 진행한다.
df2
df2.mean(axis = 1)
df2.max(axis = 1)
df2.min(axis = 1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>140</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>136</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>164</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>168</td>
    </tr>
    <tr>
      <th>열합계</th>
      <td>48</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
      <td>1216</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>432</td>
      <td>594</td>
      <td>450</td>
      <td>432</td>
      <td>270</td>
      <td>180</td>
      <td>90</td>
      <td>288</td>
      <td>10944</td>
    </tr>
  </tbody>
</table>
</div>






    0             19.444444
    1             18.888889
    2             22.777778
    3             23.333333
    열합계          168.888889
    ColTotal    1520.000000
    dtype: float64






    0             140
    1             136
    2             164
    3             168
    열합계          1216
    ColTotal    10944
    dtype: int64






    0            0
    1            2
    2            0
    3            0
    열합계         10
    ColTotal    90
    dtype: int64



### df2의 새로운 행과 열 추가
- 새로운 열 추가 : 기본인덱싱 사용
    - df['새로운열이름'] = 값
- 새로운 행 추가 : loc인덱서
    - df.loc['새로운 행 인덱스'] = 값


```python
df2['RowTotal'] = df2.sum(axis = 1)
df2

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>252</td>
    </tr>
    <tr>
      <th>열합계</th>
      <td>48</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
      <td>1824</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>432</td>
      <td>594</td>
      <td>450</td>
      <td>432</td>
      <td>270</td>
      <td>180</td>
      <td>90</td>
      <td>288</td>
      <td>16416</td>
    </tr>
  </tbody>
</table>
</div>




```python
#새로운 추가 (loc인덱서 사용이 가장 간단함)
#행이름 : ColTotal
df2.loc['ColTotal'] =  df2.sum(axis = 0)

```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-158-f9d9910c091f> in <module>
          2 #행이름 : ColTotal
          3 df2.loc['ColTotal'] =  df2.sum(axis = 0)
    ----> 4 del df2.loc['열합계']
    

    AttributeError: __delitem__


### 행/열 삭제 - df의 drop() 사용 예제

- df.drop('행이름',0) : 행삭제 
    - 행삭제 후 df로 결과를 반환
- df.drop('열이름',1) : 열 삭제
    - 열삭제 후 df로 결과를 반환
- 원본에 반영되지 않으므로  원본수정하려면 저장 해야 함
- del명령어는 삭제 명령어이며 원본을 변경 함



```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>252</td>
    </tr>
    <tr>
      <th>열합계</th>
      <td>48</td>
      <td>66</td>
      <td>50</td>
      <td>48</td>
      <td>30</td>
      <td>20</td>
      <td>10</td>
      <td>32</td>
      <td>1824</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.drop('ColTotal',0) #행 삭제 후 결과를 반환
df2 #원본 데이터에는 반영되지 않는다
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>252</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>252</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.drop('RowTotal',1) #해당열 삭제한 결과를 반환
df2 #원본에는 반영되지 않는다
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>252</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>



### NaN 값 처리 함수

- df.dropna(axis=0/1)
    - NaN 값이 있는 열 또는 행을 삭제
    - 원본 반영되지 않음
    
- df.fillna(채우려는 값)
    - NaN값을 정해진 값으로 채움
    - 원본 반영되지 않음


```python
#df2에 결측치 값 적용
df2.iloc[0,0] = np.nan
df2.iloc[2,7] = np.nan
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>NaN</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>252</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792.0</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528.0</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>




```python
#dropna : NaN이 포함된 행을 삭제
df2.dropna()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>204</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>252</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792.0</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528.0</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>




```python
#dropna : NaN이 포함된 열을 삭제
df2.dropna(axis = 1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>252</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.fillna(0)
df2
df2.fillna(5)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>0.0</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>252</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792.0</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528.0</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>NaN</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>252</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792.0</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528.0</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>5.0</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>252</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792.0</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528.0</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.fillna('a')[0].dtype
```




    dtype('O')




```python
# df의 원소 dtype 변경 함수
# df.astype(자료형) int/float

df2.fillna(0).astype(int)
df2
df2.fillna(5).astype(float)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>252</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7.0</td>
      <td>210</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2.0</td>
      <td>204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>NaN</td>
      <td>246</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>252</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792.0</td>
      <td>1089</td>
      <td>825</td>
      <td>792</td>
      <td>495</td>
      <td>330</td>
      <td>165</td>
      <td>528.0</td>
      <td>30096</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>RowTotal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>210.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>204.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>246.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>252.0</td>
    </tr>
    <tr>
      <th>ColTotal</th>
      <td>792.0</td>
      <td>1089.0</td>
      <td>825.0</td>
      <td>792.0</td>
      <td>495.0</td>
      <td>330.0</td>
      <td>165.0</td>
      <td>528.0</td>
      <td>30096.0</td>
    </tr>
  </tbody>
</table>
</div>



### 열 또는 행에 동일한 연산 반복 적용할 때 : apply() 함수
- apply() 함수는 DataFrame의 행이나 열에 복잡한 연산을 vectorizing할 수 있게 해주는 함수로 매우 많이 활용되는 함수임
- 동일한 연산을 모든열에 혹은 모든 행에 반복 적용하고자 할때 사용

- apply(반복적용할 함수, axis=0/1)
    - 0 : 열마다 반복
    - 1 : 행마다 반복 
    - 생략시 기본값 : 0



```python
#예제 df 생성
df3 = pd.DataFrame({
    'a':[1,3,4,3,4],
    'b':[2,3,1,4,5],
    'c':[1,5,2,4,4]
})
df3

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
#df3의 각 열에 대해서 np.sum 이라는 함수를 반복 적용하는 코드를 생성하시오

df3.apply(np.sum)
```




    a    15
    b    15
    c    16
    dtype: int64




```python
#df3의 각 행에 대해서 np.sum 이라는 함수를 반복 적용하는 코드를 생성하시오

df3.apply(np.sum,1)
```




    0     4
    1    11
    2     7
    3    11
    4    13
    dtype: int64




```python
df3.sum() #위 코드들과 같은 결과를 반환
```




    a    15
    b    15
    c    16
    dtype: int64



- 데이터프레임의 기본 집계함수(sum, min, max, mean 등)들은 행/열 단위 벡터화 연산을 수행함
    - apply() 함수를 사용할 필요가 없음


- 일반적으로 apply() 함수 사용은 복잡한 연산을 해결하기 위한 lambda 함수나 사용자 정의 함수를 각 열 또는 행에 일괄 적용시키기 위해 사용


#### 1회성 함수인 lambda함수를 apply()에 사용하는 예제


```python
#집합 데이터(시리즈)의 최대값과 최소값의 차이를 구하는 연산을 lambda함수로 정의
diff = lambda x: x.max()- x.min()
```


```python
#df3의 a열의 최대값과 최소값의 차이를 위에서 생성한 lambda함수를 이용해서 구하시오

diff(df3['a'])
```




    3




```python
# apply 함수를 이용하여 위에서 생성한 lambda diff를 df3의 모든 열에 반복 적용하여 
# 모든 열의 최대값과 최소값의 차이를 구하시오

df3.apply(diff,0)

```




    a    3
    b    4
    c    4
    dtype: int64




```python
# apply 함수를 이용하여 위에서 생성한 lambda diff를 df3의 모든 행에 반복 적용하여 
# 모든 열의 최대값과 최소값의 차이를 구하시오
```


```python
df3.apply(diff,1)
```




    0    1
    1    2
    2    3
    3    1
    4    1
    dtype: int64




```python
# 다른 방법 : 직접 연산

#df3 각 행에 대하여 최대값과 최소값의 차이를 구하시오
df3.max(axis=1) - df3.min(axis=1)
```




    0    1
    1    2
    2    3
    3    1
    4    1
    dtype: int64




```python
#df3의 각 열의 데이터에 대해서 카테고리 세기를 수행하시오
df3.value_counts()
```




    a  b  c
    1  2  1    1
    3  3  5    1
       4  4    1
    4  1  2    1
       5  4    1
    dtype: int64




```python
#apply함수를 사용해서 value_counts() 적용 test

df3.apply(pd.value_counts)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.0</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.0</td>
      <td>1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#df3의 각 열의 데이터에 대해서 카테고리 세기를 수행하소 NaN값은 0으로 변환 후 반환되는 
#전체 데이터의 타입을 정수로 변환하시오
df3.apply(pd.value_counts).fillna(0).astype(int)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



#### 관측 데이터 값을 범주형 데이터(카테고리) 값으로 변환
- 값의 크기를 기준으로 하여 카테고리 값으로 변환하고 싶을 때
    - pd.cut(data, bins, label)
        - data : 구간을 나눌 실제 관측 값
        - bins : 구간 경계값
        - label : 카테고리 값
    


```python
#data 값
ages = [0,0.5,4,6,4,5,2,10,21,36,15,37,31,61,20,41,31,100]
```


```python
#label : 카테고리 명
labels=['영유아','미성년자','청년','중년','장년','노년']

#bins : 구단 경계값
bins = [0,4,15,25,35,60,100]

#라벨과 빈스의 구간별 순서를 동일하게 해야한다.
#0<영유아<=4
#4<미성년자<=15
```


```python
#함수 적용해서 카테고리 생성
cuts = pd.cut(ages,bins = bins,labels=labels)
cuts
# cuts = pd.cut(ages,bins,labels)
# cuts
```




    [NaN, '영유아', '영유아', '미성년자', '영유아', ..., '노년', '청년', '장년', '중년', '노년']
    Length: 18
    Categories (6, object): ['영유아' < '미성년자' < '청년' < '중년' < '장년' < '노년']




```python
list(cuts)
```




    [nan,
     '영유아',
     '영유아',
     '미성년자',
     '영유아',
     '미성년자',
     '영유아',
     '미성년자',
     '청년',
     '장년',
     '미성년자',
     '장년',
     '중년',
     '노년',
     '청년',
     '장년',
     '중년',
     '노년']



##### Categorical 클래스 객체
- 카테고리명 속성 : Categorical.categories
- 코드 속성 : Categorical.codes 
    - 인코딩한 카테고리 값을 정수로 갖는다.



```python
type(cuts)
```




    pandas.core.arrays.categorical.Categorical




```python
cuts.categories
```




    Index(['영유아', '미성년자', '청년', '중년', '장년', '노년'], dtype='object')




```python
cuts.codes #codes의 원소가 -1이면 카테고리를 정하지 못했다는 뜻(결측값)
```




    array([-1,  0,  0,  1,  0,  1,  0,  1,  2,  4,  1,  4,  3,  5,  2,  4,  3,
            5], dtype=int8)




```python
#age list를 이용해서 df 생성
df4 = pd.DataFrame(ages, columns = ['ages'])
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>21.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>36.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>15.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>37.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>31.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>61.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>41.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>31.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4['연령대'] = pd.cut(df4.ages,bins= bins,labels=labels)
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ages</th>
      <th>연령대</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.5</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.0</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.0</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.0</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2.0</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10.0</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>8</th>
      <td>21.0</td>
      <td>청년</td>
    </tr>
    <tr>
      <th>9</th>
      <td>36.0</td>
      <td>장년</td>
    </tr>
    <tr>
      <th>10</th>
      <td>15.0</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>11</th>
      <td>37.0</td>
      <td>장년</td>
    </tr>
    <tr>
      <th>12</th>
      <td>31.0</td>
      <td>중년</td>
    </tr>
    <tr>
      <th>13</th>
      <td>61.0</td>
      <td>노년</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20.0</td>
      <td>청년</td>
    </tr>
    <tr>
      <th>15</th>
      <td>41.0</td>
      <td>장년</td>
    </tr>
    <tr>
      <th>16</th>
      <td>31.0</td>
      <td>중년</td>
    </tr>
    <tr>
      <th>17</th>
      <td>100.0</td>
      <td>노년</td>
    </tr>
  </tbody>
</table>
</div>



##### 구간 경계선을 지정하지 않고 데이터 개수가 같도록 지정한 수의 구간으로 분할하기 :  qcut()  

- 형식 : pd.qcut(data,구간수,labels=[d1,d2....])
    
    
    - 예)1000개의 데이터를 4구간으로 나누려고 한다면
        - qcut 명령어를 사용 한 구간마다 250개씩 나누게 된다.
        - 예외)같은 숫자인 경우에는 같은 구간으로 처리한다.



```python
data = np.arange(1000)
la = [1,2,3,4,5,6,7,8,9,10]
pd.qcut(data,10,labels=la)
```




    [1, 1, 1, 1, 1, ..., 10, 10, 10, 10, 10]
    Length: 1000
    Categories (10, int64): [1 < 2 < 3 < 4 ... 7 < 8 < 9 < 10]




```python
# 랜덤정수 20개를 생성하고 생성된 정수를 4개의 구간으로 나누시오.

# 각 구간의 label은 Q1,Q2,Q3,Q4 로 설정하시오.

#랜덤정수 생성 : 범위 0-19, size =20
#seed 설정해서 재 실행해도 랜덤정수가 변하지 않도록 생성
np.random.seed(3)
data = np.random.randint(20,size=20)
lb = ['Q1','Q2','Q3','Q4']
qcat = pd.qcut(data,4,labels = lb)
qcat
```




    ['Q3', 'Q2', 'Q2', 'Q1', 'Q4', ..., 'Q1', 'Q1', 'Q1', 'Q4', 'Q2']
    Length: 20
    Categories (4, object): ['Q1' < 'Q2' < 'Q3' < 'Q4']




```python
pd.value_counts(qcat)
```




    Q1    5
    Q2    5
    Q3    5
    Q4    5
    dtype: int64




```python
list(qcat)
```




    ['Q3',
     'Q2',
     'Q2',
     'Q1',
     'Q4',
     'Q3',
     'Q3',
     'Q3',
     'Q3',
     'Q2',
     'Q1',
     'Q4',
     'Q2',
     'Q4',
     'Q4',
     'Q1',
     'Q1',
     'Q1',
     'Q4',
     'Q2']



### 인덱스 설정 함수
#### 데이터 프레임 인덱스 설정을 위해 set_index(), reset_index()
- set_index() : 기존 행 인덱스를 제거하고 데이터 열 중
하나를 인덱스로 설정해주는 함수
- reset_index() : 기존 행인덱스를 제거하고 기본인덱스로 변경
- 기본인덱스 : 0부터 1씩 증가하는 정수 인덱스
    - 따로 설정하지 않으면 기존 인덱스는 데이터열로 추가 됨



```python

df3

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
#df3의 a열을 인덱스로 설정하시오
df3.set_index('c')
df3
df3 = df3.set_index('a')
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
    <tr>
      <th>c</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
#df3의 행 인덱스를 제거하고 기본 인덱스로 설정 - reset_index()
df3.reset_index()

#기존 index의 처리 : drop=True -> 기존 index 제거
#                  : 명시하지 않으면 열 data로 정의

df3.reset_index(drop=True)
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# index 원소 변경하기 : df.rename()사용
#df.rename(index={현재인덱스:바꿀인덱스})
df3 = df3.reset_index(drop=True)


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>z</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.rename(index={1:'z'})
df3.rename(columns={'b':'학생'})
df3.rename(columns={'b':'학생'},index={1:'z'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>z</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>학생</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>학생</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>z</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### list 내포 연산

#### list 내포 for문 : 문법
- [표현식(연산식) for 항목 in 반복가능객체 if 조건문]
- if 조건문은 생략 가능하다.
- 반복가능객체 : 리스트, 튜플,딕셔너리,range()등



```python
a = [1,2,3,4]

#위 list의 각 원소에 대해 2배한 원소값을 만들고 result라는 변수에 저장하시오

result = []
for i in a:
    result.append(i*2)

result
```




    [2, 4, 6, 8]




```python
# 내포 for문 사용
result2 = [i*2 for i in a]
result2
```




    [2, 4, 6, 8]




```python

```
