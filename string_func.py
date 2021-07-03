#len() : 문자열의 길이 반환
str = "erwer"
print(len(str))

#count() : 문자열 내에 있는 특정 문자의 개수 반환
print(str.count('e'))

#find() : 문자열 내에서 문자열이 존재하는지 여부와 문자열의 시작 위치를 반환한다.
##문자열이 존재하면 시작위치 반환 / 미존재시 -1 반환
crawling = 'Data Crawling is Fun'
print(crawling.find('Fun')) #문자열의 시작 위치 반환
print(crawling.find('a')) #중복 문자 존재 시 가장 앞의 문자 위치 반환
print(crawling.find('z')) #-1 반환

#index() : 문자열 내에서 특정 문자열의 시작 위치 반환
crawling = 'Data Crawling is Fun'
print(crawling.index('Fun'))
#find 함수와 비슷한 기능

#split : 구분자를 기분으로 문자열을 나눔
#나눈결과를 list로 만들어 반환한다
string = "Python Programming"
print(string.split('-'))

names = "홍길동, 이몽룡, 성춘향, 변학도"
names_split = names.split(',')
print(names_split) #['홍길동', ' 이몽룡', ' 성춘향', ' 변학도']

colors = 'red:blue:yellow:green'
colors_split = colors.split(':' )
print(colors_split) #['red', 'blue', 'yellow', 'green']

#replace() : 전체 문자열에서 특정 문자열을 찾아 다른 문자열로 변경해주는 함수
#문자열.replace(찾는 문자열, 변경할 문자열)
course = 'Java Programming'
#Java => Python
print(course.replace('Java','Python')) #Python Programming

#join() :d 각 문자 사이에 특정 문자를 삽입하는 함수
a = '---'
b = 'abc'
print(b.join(a)) #-abc-abc-
print('-'.join(b)) #a-b-c

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