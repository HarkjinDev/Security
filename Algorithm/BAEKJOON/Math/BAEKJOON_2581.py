# 소수
# https://www.acmicpc.net/problem/2581

import math

M = int(input())
N = int(input())

result = []

for i in range(M, N + 1):
    check  = 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            check = 0
            break
    if check and i != 1:
        result.append(i)
if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)