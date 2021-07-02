#list를 함수의 인수로 전달할 때
def show_list(func_list): #list 변수의 주소가 전달되면서 같은 리스트를 참조하게 된다.
    func_list[0]=10 #원본인 my_list에도 영향을 끼친다.
    print(func_list)
    func_list = [10,20,30,40] #list 전체를 변경하면 원본에는 변화를 주지 못한다.
    print(func_list)

my_list=[1,2,3,4]
show_list(my_list)
print(my_list)

########################################################################################

student = [{'name':'홍길동', 'korean': 87, 'math': 98, 'english': 88, 'science': 95},
           {'name':'이몽룡', 'korean': 92, 'math': 92, 'english': 96, 'science': 98,},
           {'name':'성춘향', 'korean': 76, 'math': 76, 'english': 94, 'science': 90,},
           {'name':'변학도', 'korean': 98, 'math': 92, 'english': 96, 'science': 92,},
           {'name':'박지성', 'korean': 95, 'math': 98, 'english': 98, 'science': 98,},
           {'name':'류현진', 'korean': 64, 'math': 88, 'english': 92, 'science': 92,}
           ]

#딕셔너리를 전달 받아서 딕셔너리의 일부만 추출 후 딕셔너리 구성
def get_studentinfo(std_list):
    name = std_list['name']
    korean = std_list['korean']
    return {'name':name,'korean':korean}

for i in student:
    student_info = get_studentinfo(i)


std_sublist=[]
for i in student:
    student_info = get_studentinfo(i)
    std_sublist.append(student_info)

print(std_sublist)