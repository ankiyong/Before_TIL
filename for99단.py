#구구단의 단수를 입력받아서 해당 구구단을 출력하는 프로그램 작성

dan = int(input('단 수 입력 : '))
for i in range(1,10):
    print('%d * %d = %d' % (dan,i,dan*i))