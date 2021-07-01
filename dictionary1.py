#딕셔너리 기본형
d = {1:'a',2:'b'}
print(d) #{1: 'a', 2: 'b'}

#item추가 (key -2, value -'b')
d[3] = 'c'
print(d) #{1: 'a', 2: 'b', 3: 'c'}

#key는 문자도 가능
d['test'] = 'test1'
print(d) #{1: 'a', 2: 'b', 3: 'c', 'test': 'test1'}

#딕셔너리 주요 함수
#딕셔너리.keys()   > 딕셔너리 내 모든 key를 리스트로 반환
#딕셔너리.values() > 딕셔너리 내 모든 value를 리스트로 반환
#딕셔너리.items()  > 딕셔너리 내 모든 item을 튜플로 반환

print(d.keys()) #dict_keys([1, 2, 3, 'test'])
print(d.values()) #dict_values(['a', 'b', 'c', 'test1'])
print(d.items()) #dict_items([(1, 'a'), (2, 'b'), (3, 'c'), ('test', 'test1')])

#list,tuple로 변환
to_list = list(d.keys())
print(type(to_list))
to_tuple = tuple(d.keys())
print(type(to_tuple))

#딕셔너리 내의 특정 item value 참조 : key이용
member = {'name':'홍길동','phone':'1234-1234','birth': '10/15' }
print(member['name'])

#key리스트의 각 요소 출력
for key in member.keys():
    print(key,end=" ")

#value값 출력
for value in member.values():
    print(value,end=" ")

#item 출력
for item in member.items():
    print(item,end="")