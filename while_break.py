#무한 루프 탈출을 위한 break

while True:
    print('반복 수행되는 문장')
    answer = input('x를 입력하면 종료 : ')
    if answer == 'x':
        break

print('종료!')