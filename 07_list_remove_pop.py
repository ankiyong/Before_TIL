n = [1,2,3,4,5,6,6,4]
n.remove(4) #가장 앞에 존재하는 4를 삭제하고 원본 반영됨
print(n) # [1, 2, 3, 5, 6, 6, 4]

#n list에서 원소값이 6인 원소를 모두 제거하시오
#6의 개수 확인
count = n.count(6)
print(count)
for i in range(count):
    n.remove(6)
    print('6삭제',n)
print(n)

# n1 = [1,1,1,3,2,4]
# n1.remove(1)
# n1.remove(1)
# n1.remove(1)
# n1.remove(1)
# print(n1) => 요소값이 없는데 제거하면 오류가 난다
#제거하기 전에 반드시 요소가 있는지 확인하는게 좋다

#####################################################
#pop() : 리스트 마지막 요소를 반환하고 삭제
x = ['a','b','c','d']
y = x.pop() #d
print(y)
print(x)

#x에 남아있는 요소 3개를 pop
#계속 pop을 실행해서 더이상 요소가 ㅇ벗으면 빈리스트로 남게됨
x.pop()
x.pop()
x.pop()
print(x)

#x가 빈리스트인경우 pop()
# x.pop()
# print(x) => 에러 발생

#pop(인덱스) : 인덱스 위치에 있는 요소 반환 삭제
heros=['슈퍼맨','아이언맨','스파이더맨','헐크','토르']
tmp = heros.pop(2)
print('삭제된 값 : ',tmp)
print(heros)
