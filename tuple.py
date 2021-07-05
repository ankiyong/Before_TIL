##Tuple
#list와 유사한 자료형이지만 원소 변경,추가 및 삭제가 불가능함

#tuple만들기
t1 = (1,2,3)
print(t1) #(1,2,3)

t2 = (1,2,3,t1)
print(t2) #(1, 2, 3, (1, 2, 3))

list1 = [1,2,3,t1]
print(list1) #[1, 2, 3, (1, 2, 3)] #list안에 tuple 삽입 가능

list1[3] = 10
print(list1) #[1, 2, 3, 10]

#괄호가 없어도 tuple 생성 가능
t3 = 2,3,4
print(type(t3)) #<class 'tuple'>

#tuple를 list로 변환하기
t4 = 2,3,4
print(list(t4)) #[2, 3, 4]