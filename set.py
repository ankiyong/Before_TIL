#집합 만들기 : {} 사용
s1 = {1,2,3,4}
print(s1) #{1, 2, 3, 4}
print(type(s1)) #<class 'set'>

#list형과 tuple형을 set형으로 변환
s2 = set([10,29,30])
print(s2) #{10, 29, 30}
s2 = set((19,2390,230))
print(s2) #{19, 2390, 230}

#set는 중복값이 있으면 제거하고 출력한다
s4 = {1,2,3,3,4,5,}
print(s4) #{1, 2, 3, 4, 5}

#set내에 list포함시 에러가 발생한다
# s5 = {1,2,3,[1,2],4}
# print(s5) #TypeError: unhashable type: 'list'

#set는 항목의 순서가 없는 집합형태로 인덱스 사용이 불가능하다

#집합에 요소 추가 - add,update
s = {1,2,3}
s.add(4)
print(s) #{1, 2, 3, 4}

s.update([6,7]) #update는 개별숫자가 아닌 묶인 숫자만 추가 가능
print(s) #{1, 2, 3, 4, 6, 7}
s.update((9,8))
print(s) #{1, 2, 3, 4, 6, 7, 8, 9}

#집합에 요소 제거 - remove,discard
s.remove(3)
print(s) #{1, 2, 4, 6, 7, 8, 9}
s.discard(4)
print(s) #{1, 2, 6, 7, 8, 9}

#집합의 전체 요소 삭제
s.clear()
print(s) #set()

#집합변수 완전 삭제
del s
print(s) #NameError: name 's' is not defined