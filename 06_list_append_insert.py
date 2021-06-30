append()
a = [1,2,3,4]
a.append(5) # a list마지막 원소로 5을 추가하고 a에 저장(원본변경)
print(a) # [1,2,3,4,5]

a.append([6,7])
print(a)

# a.append(8,9) #원소를 2개 추가
# print(a) => 에러


#빈 리스트 생성하고 요소를 나중에 추가하려고 함
empty = []
empty.append(10)
print(empty)

#사용자에게 5개의 값을 입력 받아서 리스트에 저장하는 코드

a1 = [] #값을 저장할 빈 리스트
for i in range(0,5):
    num = int(input('값을 입력하세요 : '))
    a1.append(num)
    print('%d번째 입력결과 : %d' % (i+1,num))
print(a1)

#위 코드에서 입력받은 값을 각 요소로 출력하는 코드로 작성하시오

for a in a1:
    print(a)

for i in range(len(a1)):
    print(a1[i])


#####################################################
#insert(위치,값) : 리스트 특정 위치에 요소 삽입
nums = [1,2,3,4,5]
nums.insert(1,238945905) #인덱스값 1번에 삽입,기존 인덱스 1번 이상부터는 하나씩 위치가 밀림)
print(nums)

nums.insert(-1,'홍길동')
print(nums)

#insert 함수를 이용해서 맨뒤에 삽입
nums.insert(len(nums),12.3)
print(nums)

nums.insert(len(nums)-1,[10,20])
print(nums)