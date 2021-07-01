# #함수 정의 문법
# def 함수명():
#     함수 호출시 실행될 문장1
#     함수 호출시 실행될 문장1
#     return 반환값(생략 가능)

def show_info():
    print('성명 : 안기용')
    print('나이 : 20')

show_info()

#함수정의
#함수 이름 : sum()
#함수 기능 : 사용자로 부터 2개의 정수를 입력 받아 더한 결과를 반환

def sum():
    num1 = int(input('정수1 : '))
    num2 = int(input('정수2 : '))
    return num1+num2
a = sum()
print(a)

#return 값이 없을 때 변수에 저장하면 결과가 출력되지 않는다.

#여러개의 값 반환하기
def multi_return():
    return 1,2,3

b = multi_return()
print(b) # (1, 2, 3) tuple로 반환됨

#리스트 반환
#함수명 : get_names()
#함수 기능 : 사용자로 부터 3명의 회원 이름을 입력 받아 리스트에 추가한 후

def get_names():
    names = []
    for i in range(3):
        name = input('이름 입력 : ')
        names.append(name)
    return names

name_list = get_names()
print(name_list)


#dict반환
#함수 이름 : get_info()
#함수 기능 : 사용자로 부터 이름과 나이를 입력받아 딕셔너리로 저장하고
#저장된 딕셔너리 데이터를 반환하는 함수

def get_info():
    name = input('이름 입력 : ')
    age = input('나이 입력 : ')
    student = {'이름':name,'나이':age}
    return student

stu_info = get_info()
print(stu_info)