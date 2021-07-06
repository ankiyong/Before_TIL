#에러 종류와 상관없이 모든 에러 처리
#try~exception 구문
try:
    a = 10/0
except:
    print('오류발생!') #오류발생시 출력
else:
    print(a) #오류발생하지 않을시 출력
finally:
    print('수고하셨습니다.') #오류에 관계없이 항상 출력

#오류발생시 아무것도 하지 않고 넘어가기
try:
    a = 10/0
except:
    pass #pass 명령어를 통해 오류가 발생해도 아무런 조치를 취하지 않게 된다.

finally:
    print('수고하셨습니다.') #오류에 관계없이 항상 출력