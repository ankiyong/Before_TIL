# TIL

2021/06/30

### 리스트

리스트 관련 함수

```pyhton
#len() : list의 길이를 반환
a = [1,2,4]
print('전체 원소의 개수 : ', len(a))
#count() : list 내의 특정 요소의 개수 세기
#list.count(요소)
print('원소 1의 개수 : ' , a.count(1)) # 1이라는 요소의 개수를 세라~

################################################
#append() :list의 끝에 새로운 요소 추가
#list.append(새로추가할요소)

#insert() :list의 특정 위치에 요소를 삽입함
#list.insert(삽입위치,추가요소)

#06_list_append_insert.py에 정리

#################################################
#remove() : list에서 값에 해당되는 요소를 제거함
#list.remove(제거할 요소 값)
#동일한 값이 여러개 있는 경우에는 첫번째 만나는 값만 제거함
#동일한 값 모두 제거 시 for문 사용

#pop() : list의 마지막 요소를 반환하고 삭제/인덱스 위치에 있는 요소를 반환하고 삭제
#값을 반환하고 삭제
#리스트.pop()
#리스트.pop(인덱스값)

#07_list_remove_pop.py에 정리

##############################################
#extend() : list의 확장
#리스트.extend()
#이전 리스트에 원소 추가하여 확장된 리스트로 됨
#원래 리스트 변경
a=[1,2,3]
a.extend([4,5]) #[1, 2, 3, 4, 5]
print(a)

b=[1,2,3]
b.append([4,5]) #[1, 2, 3, [4, 5]]
print(b)

#extend는 원소가 추기되면서 리스트가 확장된다 - 하나의 리스트
#append는 추가된 원소가 리스크면 하위 리스트로 추가됨 - 리스트 안의 리스트
#################################################
#sort,reverse,sorted
#08_list_sort.py에 정리

##################################################
#index() : list안에서 원소의 위치 값 반환
#리스트.index(값)
a=[1,2,3,4,5,5]
print(a.index(3)) #2번 인덱스
print(a.index(5)) #4번 인덱스,가장 앞의 원소 위치 반환함
# print(a.index(10)) => 오류

##################################################
#min() : list내에서 최소값 원소 반환
#max() : list내에서 최대값 원소 반환
n = [100,7,-2,99,30]
char = ['c','a','D','A','b']
n_char = [1,300,'a','D','-2']

print(min(n))
print(max(n))

print(min(char))
print(max(char))

# print(min(n_char))
# print(max(n_char))

#in/not in(포함여부 판단 후 True/False로 반환)
num = [1,2,3,4,5]
result = 2 in num
print(result) #True

result = 2 not in num
print(result) #False

#리스트 일치 검사
#비교 연산자 사용해서 2개의 list비교 가능
#첫번째 요소 부터 비교를 시작
#첫번째 요소의 비교에서 결과가 False 면 더이상 비교하지 않고
#True면 두번째 요소 비교 ..
#list 내의 모든 요소 비교 결과가 True면 전체결과 : True

list1=[1,2,3]
list2=[1,2,3]
print(list1 == list2) #요소값이 하나라도 다르면 False 반환
```

### 튜플

```python
# 튜플 (Tuple)
# 리스트와 유사한 집합적 자료형이지만
# 리스트와 달리 원소 변경 불가
# 추가 / 수정 / 삭제 다 안 됨
# 소괄호 () 사용
# 튜플 = (값1, 값2, … , 값n)
# colors = ("red", "green", "blue")
# numbers = (1, 2, 3, 4, 5 )
# 각 원소는 인덱스(Index)로 구분(인덱스: 0부터 시작)
# 원소 변경 시 에러
# numbers[0] = 10 #오류


#튜플 만들기 - 소괄호 이용

t1 = (1,2,3)
print(t1)

list1 = [1,2,3,t1]
print(list1) #[1, 2, 3, (1, 2, 3)]

list1[3] = 10
print(list1)

#괄호가 없어도 튜플로 생성
t2 = 3,4,5
print(t2)

#튜플 내에 튜플 삽입 가능
t3 = t1,(7,8,9)
print(t3)

#list로 튜플 생성
t4 = [1,2],[3,4]
print(t4)

t4_1 = 3, #하나의 원소를 갖는 튜플로 생성 t4_1 = (3)
print(type(t4_1)) #=> <class 'tuple'>


#함수를 이용해서 튜플 생성(list형을 튜플 형으로 변환)
t5 = tuple([5,6,7,8])
print(t5)


#print(int('15'))


# t6 = tuple(3)
# print(t6) TypeError: 'int' object is not iterable

#튜플을 list로 변환
#(1,2,3) -> [1,2,3]
t1 = (1,2,3)
to_list1 = list(t1)
print(to_list1)

#여러개의 튜플을 ilst로 변환
t3 = ((1,2,3),(7,8,9))
to_list2 = list(t3)
print(to_list2) # [(1, 2, 3), (7, 8, 9)]

#list를 tuple로 변환
list = [1,2,3]
to_list = tuple(list)
print(to_list)

#tuple은 수정이 불가능하다
# to_list[0] = 10
# print(to_list) TypeError: 'tuple' object does not support item assignment
```



### 집합 (set)

```python
#집합 만들가 : {} 이용
s1 = {1,2,3,4,5}
print(s1)
print(type(s1)) #<class 'set'>

#set() 함수로 집합 만들기
#list형을 set형으로 형변환은 가능하다
s2 = set([10,20,30])
print(s2)
print(type(s2)) #<class 'set'>

#tuple형을 set형으로 형변환
s3 = set((100,200,300))
print(s3) #{200, 100, 300} 입/출력 순서가 다를 수 있음
print(type(s3)) #<class 'set'>

#중복값이 있으면 제거하고 표시한다
s4 = {1,2,3,3,4}
print(s4) #{1, 2, 3, 4}

#set 내에 list 포함 시 에러 발생
# s5 = {1,2,[3,4]}
# print(s5) TypeError: unhashable type: 'list'

#인덱스 사용 불가
# print(s4[0]) TypeError: 'set' object is not subscriptable

#집합에 요소 추가(add 함수 사용) -1개
s={1,2,3}
s.add(4)
print(s) #{1, 2, 3, 4}

#집합에 요소 추가(update 함수 사용) -여러개
s.update([5,6])
s.update((5,6))
# s.update(5) #=> 개별 숫자 말고 묶인 숫자만 추가 가능
print(s) #{1, 2, 3, 4, 5, 6}

#요소 제거
s.remove(3)
print(s) #{1, 2, 4, 5, 6}

#전체 요소 삭제
s.clear()
print(s) #set() : 빈 집합의 의미

#집합 변수 완전 삭제
del s #변수 삭제됨
```

##### 집합의 특징순서가 없다

입력되는 순서와 출력되는 순서가 다를 수 있음
동일한 요소(값)이 중복될 수 없다
인덱스 사용 불가
이미 포함되어 있는 요소(값)를  변경할 수 없음 
요소 추가/삭제는 가능
집합 안에 변경 가능한 항목 포함할 수 없음
리스트 포함할 수 없음
튜플은 포함 가능
튜플은 변경 불가하기 때문