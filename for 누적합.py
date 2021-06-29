#1부터 10까지 출력하고 그 누적합을 출력하는 프로그램 생성
sumi = 0
for i in range(1,11):
    print(i)
    sumi += i
print('1부터 10까지 누적합 = %d' % sumi)