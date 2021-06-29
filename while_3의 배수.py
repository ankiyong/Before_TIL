i = 0
sumi = 0
while i < 101:
    i +=1
    if i % 3 == 0:
        sumi += i
print('1부터 100까지 모든 3의 배수의 합은 : %d' % sumi)