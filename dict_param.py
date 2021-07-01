#인수(인자)와 매개변수 정리

#인수(인자) : argument
#함수에게 실제로 전달되는 값(호출할 때 전달하는 값)
#print('hello') - 'hello' => 인자

#매개변수(parameter)
#함수를 호출할 때 전달되는 실제 값을 받아 저장하는 변수

def add(num1,num2): #num1,num2 => 매개변수
    print('합 : %d ' % (num1+num2))

add(10,20) #10,20 => 인수(인자)

def show_name(name):
    print(name)

show_name('안기용')
show_name(123) #매개변수도 인자값의 데이터 형태에 따라 형태가 결정된다

#매개변수(파라미터)와 반환값이 있는 함수의 정의
#함수 이름 : get_average(k,e,m)
#함수 기능 : 파라미터 변수 3 값에 대한 평균을 계산한 후 계산된 평균을
#반환하는 것

def get_average(k,e,m):
    return (kor+eng+math)/3

kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
math = int(input('수학 점수 : '))
print(get_average(kor,eng,math))


#디폴트 매개변수(파라미터)
#매개변수에 기본값 지정 - 호출할 때 인수가 넘어오면 넘어오는 인수 사용
#인수가 안넘어 오면 기본값을 사용

def greet(name,msg='hello'):
    print(name+','+msg)

greet('안기용') #안기용,hello <~ 두번째 매개변수 값을 설정 안해서 기본값이 출력됨

#디폴트 매개변수 2개 사용

def show_info(name,year=4,age=23):
    print(name,year,age)

show_info('안기용')

#함수에 리스트를 전달
#함수 이름 : show_names(names):
#함수 기능 : 전달받은 변수의 값을 반복문을 활용해서 요소값으로 출력하시오
#리스트가 전달된다고 가정

def show_name(names):
    for name in names:
        print(name,end=" ")

name_list = ['kim','lee','choi']
show_name(name_list) # kim lee choi 출력

#함수에 딕셔너리 전달하는
#함수 이름 : show_names(names):
#함수 기능 : 전달받은 변수의 값을 반복문을 활용해서 요소값으로 출력하시오
#딕셔너리가 전달된다고 가정

def show_info(info):
    print(info)
    print('이름 : '+info['name'])
    print('주소 : '+info['address'])

info_list = {'name':'안기용','address':'seoul','age':'29'}
show_info(info_list)