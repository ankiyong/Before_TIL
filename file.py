#파일 생성: 파일명만 적으면 현재 디렉터리에 생성
#파일객체변수명 = open(파일명,모드'w')
#위 코드 실행 후 파일 핸들링하기 위해서는 파일객체 변수명을 사용해야 한다.

# 파일 생성
# 파일을 쓰기 모드(w)로 연다
# 해당 파일이 존재하지 않으면 새로 생성하고
# 존재하면 덮어 씀 (기존 내용 없어짐)

f = open('test.txt','w',encoding='utf-8') #test파일 생성
f.close()

#파일에 쓰기 : 파일을 쓰기모드(w)로 열고
#파일 객체 변수의 writw()매서드로 풀력값을 파일에 기록
data = 'hello!'

f = open('test.txt','w',encoding='utf-8')
f.write(data) #test.txt파일에 data가 기록됨
f.close()

#여러행에 걸쳐 파일에 보내기
f = open('test.txt','w',encoding='utf-8')

for i in range(1,11):
    data = '%d행\n' % i #1행2행3행4행5행6행7행8행9행10행 이 f에 기록됨
    f.write(data)
f.close()

# 파일 읽기 방법
# readline()
# 1개 행씩 읽어 오기
# 1행 끝에 ‘\n’ 포함
# readlines() :
# 모든 행을 읽어 라인 별로 잘라서 리스트 생성
# 1개 행이 1개 요소
# [‘..’, ‘…’, ‘…’, …, ‘…’]
# read()
# 내용 전체를 읽어서 문자열로 반환

#readline() : 함수를 이용해서 1개 라인 읽어오기
print('---첫 번째 행 읽기---')
f = open('test.txt','r',encoding='utf-8')
line = f.readline()
print(line) #1행
f.close()

#readline() : 함수를 이용해서 모든 라인 읽어오기
print('---파일전체읽기---')
f = open('test.txt','r',encoding='utf-8')
while True:
    line = f.readline()
    if not line:
        break
    print(line,end="")
f.close()

#파일 전체 라인을 읽어와서 다른 파일에 쓰는 코드
#2개 파일 객체 필요
f = open('test.txt','r',encoding='utf-8')
f1 = open('test1.txt','a',encoding='utf-8')

while True:
    line = f.readline()
    if not line:
        break
    f1.write(line)
    print(line,end="")