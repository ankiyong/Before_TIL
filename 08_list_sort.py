#sort() : list를 정렬, 원본 list를 변경
scores = [90,78,56,84,45]
scores.sort() #기본 : 오름차순 정렬
print(scores)

scores = [90,78,56,84,45]
scores.sort(reverse=True)
print(scores)

scores = [90,78,56,84,45]
scores.reverse() #원소의 위치를 역순으로 변경(정렬은 안함)
print(scores)

##문자의 정렬 - 대문자 < 소문자
char = ['b','A','d','C']
char.sort() #오름차순정렬
print(char) #['A', 'C', 'b', 'd']

char = ['b','A','d','C']
char.sort(reverse=True) #내림차순정렬
print(char) #['d', 'b', 'C', 'A']


#대소문자 구별 없이 정렬
#key=str.lower

char = ['b','A','d','C']
char.sort(key=str.lower)
print(char) #['A', 'b', 'C', 'd']
#
# #대소 구별없이 내림차순 정렬
# char = ['b','A','d','C']
# char.sort(key=str.lower.reverse=True)
# print(char)


#문자열은 어떻게 정렬되는지 - 첫 문자로 정렬
ids = ['SKY','Blue','red','eBook','GREEN']
ids.sort() #오름차순 정렬 - 첫 문자로 정렬
print(ids) #['Blue', 'GREEN', 'SKY', 'eBook', 'red']

#대소문자 구별 없이 정렬
ids = ['SKY','Blue','red','eBook','GREEN']
ids.sort(key=str.lower) #오름차순 정렬 - 첫 문자로 정렬
print(ids) #['Blue', 'eBook', 'GREEN', 'red', 'SKY']

#sorted() : 원본 유지하면서 저열ㄹ된 새로운 리스트 반환
a = [3,5,2,1,4]
b=sorted(a)
print('a: ' , a)
print('b: ', b)