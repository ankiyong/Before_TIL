#readlines()함수를 이용해서 전체 라인 읽어오기
f = open('test.txt','r',encoding='utf-8')
lines = f.readlines()
print(lines)
f.close()

f = open('test.txt','r',encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line,end="")
f.close()

#read()함수 : 내용 전체를 읽어서 1개의 문자열로 반환
f = open('test.txt','r',encoding='utf-8')
line = f.read()
print(line)

for i in line: #1개 문자씩 출력
    print(i)

#read() 함수를 이용해서 파일 내용을 문자열로 저장
f = open('test.txt','r',encoding='utf-8')
date = f.read()
value = input('검색값 : ')
if value in date:
    print('있음')
else:
    print('없음')
f.close()
# append : 파일 끝에 추가하는 기능
# 파일 열기모드를 a로
f = open('test.txt', 'a', encoding='utf-8')
append_data = '\nPython'
f.write(append_data)
f.close()
