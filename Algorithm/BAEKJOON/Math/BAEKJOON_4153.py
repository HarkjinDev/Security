# 직각삼각혇
#https://www.acmicpc.net/problem/4153

while True:
    A = list(map(int, input().split()))
    max_num = max(A)
    if sum(A) == 0:
        break
    A.remove(max_num)
    if A[0]**2 + A[1]**2 == max_num ** 2:
        print('right')
    else:
        print('wrong')

