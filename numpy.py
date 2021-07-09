import numpy as np

# #0부터 3까지 배열
#
#
array1 = np.arange(4)
print(array1)
#
# array2 = np.zeros((4,4), dtype=float)
# print(array2)
#
# array3 = np.ones((3,4), dtype=str)
# print(array3)
#
# #0부터 9까지 랜덤하게 초기화된 배열 만들기
#
# array4 = np.random.randint(0,10,(3,3))
# print(array4)
#
# #평균이 0이고 준편차가1인 표준정규를 띄는 배열
# array5 = np.random.normal(0,1,(3,3))
# print(array5)
#
# array6 =  np.array([1,2,3])
# array7 = np.array([4,5,6])
# array8 = np.concatenate([array7,array6])
# print(array8.shape)
# print(array8)
#
# array9 = array8.reshape(2,3)
# print(array9)
#
# array10 = np.arange(4).reshape(1,4)
# array11 = np.arange(8).reshape(2,4)
# print(array11)
# print(array10)
#
# array12 = np.concatenate([array11,array10],axis=0)
# print(array12)
array13 = np.arange(8).reshape(2,4)
left, right = np.split(array13,[2],axis=1)
print(left.shape)
print(right.shape)

print(right)
print(left)
print(array13)