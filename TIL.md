# TIL

2021-06-29

중첩for 사용

## while문의 다양한 사용

```python
#조건식이 만족하는 동안 반복을 수행(반복의 횟수가 결정안됐을때 주로 사용)

i  = 1
while i < 10:
    print(i)
    i = i + 1
print()

=>
1
2
3
4
5
6
7
8
9


#초기값이 없는 경우

while 3>1:
    print('hello')
 =>무한히 반복된다
```

```python
#while문을 이용한 조건이 있는 누적 합계
i = 1
sum = 0
while i < 101:
    if i % 3 == 0:
        sum = sum + i

    i = i + 1

print('1부터 100까지의 모든 3의 배수의 합은 : %d 입니다. ' % sum)

=>1부터 100까지의 모든 3의 배수의 합은 : 1683 입니다. 
```

```python
#사용자로부터 입력받은 숫자가 7이면 프로그램을 종료
#7이 아니면 다시 입력을 받는다


num = int(input('숫자 입력 : '))

while num!= 7:
    num = int(input('다시 입력: '))
print(num, "입력 ! 종료")
=>
숫자 입력 : 7
7 입력 ! 종료
```

```python
#무한루프
#반복문을 종료하기 위해 break문 사용

while True:
    print('반복 수행되는 문장입니다.')
    answer = input('종료하려면 x 입력 : ')
    if answer == 'x':
        break

print('종료했습니다')
=>
반복 수행되는 문장입니다.
종료하려면 x 입력 : 
```

```python
#continue 문
#반복문 수행중에 만나면 현재 시점에서 중단하고
#다음 반복을 계속 수행한다


x = 0
while x < 10:
    x+=1
    if x % 2 == 0:
        continue
    print(x)
=>
1
3
5
7
9
'''
if의 조건이 참이면 continue 발동해서 다시 처음으로 돌아감
if의 조건이 거짓이면 continue 발동 안해서 진행됨
'''
```

## 문자열 

```python
#문자열
#문자의 나열 - 여러문자로 이뤄져있기 대문에 한 문자당 하나의
#메모리 공간을 차지한다
#'abc' -> a한칸 b한칸 c한칸의 공간을 차지하고 공간이 연속되어있음
#인덱싱과 슬라이싱이 가능

#
crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'
#
# #전체 문자열 출력(반환)
#
print(crawling)
print(crawling[:])

# #특정 인덱스의 문자 출력 - 파이썬의 인덱싱은 0부터 시작한다
print(crawling[0]) #=> 1번쨰 문자
print(crawling[-1]) #=> 마지막 문자
print(crawling[2]) #=> 인덱스2번, 실제 3번째 문자

#슬리이싱 에제
#변수명[시작인덱스 : 정지+1인덱스]
print(crawling[0:4]) # => 0번 인덱스 부터 3번 인덱스 까지
print(crawling[5:16]) #=> 5번 인덱스 부터 15번 인덱스 까지
print(crawling[17:]) #=> 17번 인덱스 부터 마지막 인덱스 까지
print(crawling[19]) #=> 19번 인덱스 문자 출력
print(crawling[-1:]) #=> 시작은 마지막 문자에서 끝까지 - 마지막 문자 출력
print(crawling[:-1]) #=> 처음부터 마지막 전 문자까지
print(crawling[16:16+4]) #=> 16:20과 동일함 - 16~19 의미

print('=================================')


print(parsing) => Data parsing is also fun
print(parsing[5:]) => parsing is also fun
print(parsing[:15]) => 'Data parsing is '
print(parsing[:]) => Data parsing is also fun


#### 주의

string = 'happy day !!!'

string_a = string[:5]  #가능
strint[5] = 'abd'  #문자열의 일부분 수정 불가능
strint = 'abd'  #문자열의 전체 수정 불가능

print(string_a) => 'happy'
print(string) => 'abd'
```

## 문자열 함수 정리

```python
#len():문자열 길이 반환
string = "asdfg"
print(len(string)) => 5

#count : 문자열 내에 들어있는 특정 문자의 개수 반환
#변수(문자열).count('특정문자(열)')
print(string.count('a')) => 1
print('asdfsa'.count('d')) => 1

#find : 문자열 내에서 특정 문자열이 존재하는지 여부와 문자열의 시작 위치를 반환
#특정 문자열이 존재하면 시작 위치값 반환 / 존재하지 않으면 -1 반환
#필터링 하거나 문자열 검사, 추출할 때 주로 사용
crawling = 'Data Crawling is Fun'
print(crawling.find('Fun')) #문자열의 시작 위치 반환
print(crawling.find('F'))
print(crawling.find('z')) #-1(없음)
print(crawling.find('a'))#문자가 여러개 있어도 처음 찾은 문자의 위치를 반환함

#index : 문자열 내에서 특정 문자열의 시작 위치를 반환
crawling = 'Data Crawling is Fun'
print(crawling.index('Fun')) #문자열의 시작 위치 반환
print(crawling.index('F'))
# print(crawling.index('z')) #-1(없음)
print(crawling.index('a'))#문자가 여러개 있어도 처음 찾은 문자의 위치를 반환함

#split : 구분자를 기준으로 문자열을 나눔
#나눈 결과를 list로 만들어서 반환함
#구분자 : 기본 공백
#구분자 지정 : "-", ":" , ","

string = "Python Programming"
string_split = string.split() #구분자 : 기본 공백
print(string_split)

names = "홍길동, 이몽룡, 성춘향, 변학도"
names_split = names.split(',')
print(names_split)

colors = 'red:blue:yellow:green'
colors_split = colors.split(':')
print(colors_split)

#문자열과 list의 차이
for c in colors_split: #각 요소 출력
    print(c)
for c in colors: #문자별로 출력
    print(c)
#range()에 list사용
for i in range(0,len(colors_split)):
    print(colors_split[i])


test = '홍길동a이몽룡a성춘향a변학도'
test_split = test.split('a')
print(test_split)

#replace = 전체 문자열에서 특정 문자열을 찾아서 다른 문자열로 변경해주는 함수
#전체문자열.replace(찾는 문자열,변경할 문자열)
#찾는 문자열이 존재하면 변경된 문자열을 반환해줌
#찾는 문자열이 없으면 원래 문자열을 그대로 반환

course = 'Java Programming'
#Java => Python
print(course.replace('Java','Python'))
# 이 문장을 수행하 ㄴ수의 course 변수의 값은 변경되는가?
# => 원본은 변경되지 않는다

print(course.replace('Web','Python'))

#join : 각 문자 사이에 특정 문자(열)을 삽입하는 함수
a = 'aa'
b = 'bbb'

print(a.join(b))

print('-'.join(b))

c_str = '대한민국' #대*한*민*국
print('*'.join(c_str))


#리스트에서 join사욧ㅇ
sep = '-'
names = ['홍길동','이몽룡']
print(sep.join(names))


#upper: 대문자로 /lower: 소문자로 /capicalize: 문장의 첫 문자를 대문자로 /title : 단어의 첫 문자를 재문자로
string = 'this is MY DOG'
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())

#공백 제거
#strip : 양쪽 공백 제거 / lstrip : 왼쪽 공백 / rstrip : 오른쪽 공백 제거
s1 = '     hello     '
print('test',s1.strip(),'test')
print(s1.lstrip(),"test")
print("tset",s1.rstrip())

#isalpga : 문자 여부 결과 반환
#isdigit : 숫자 여부 결과 반환
#isspace : 하나의 문자에 대해서 공백 여부 결과 반환
#isalnum : 문자나 숫자 여부에 대한 결과 반환
#True/False로 반환됨

phone = input('전화번호 입력(숫자만) : ')
if phone.isdigit():
    pass
else:
    print('숫자만 입력하세요')

name = input('이름 입력 : ')
if not(name.isalpha()):
    print('문자만 입력하세요')

ID = input('id입력 : ')
#문자 또는 숫자가 아닌 경우 :
if not(ID.isalnum()): #문자 or 숫자 or 문자+숫자
    print('문자와 숫자만 사용할 수 있습니다')

print(''.isspace()) #스페이스 한개인 경우
print(' c'.isspace()) #다른문자 혼합
print('  '.isspace()) #스페이스 두개
```

