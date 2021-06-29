#사용자가 입력한 이름이 명단 리스트에 있는지 검색 후 결과를 출력

members = ['홍길동', '이몽룡','성춘향','변학도']
name = input('이름 입력 : ')
for member in members:
    if name == member:
        find = True
        break
    else:
        find = False
if find == True:
    print('명단에 있습니다.')
else:
    print('명단에 없습니다.')