# 손익분기점
# https://www.acmicpc.net/problem/1712

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(int(A/(C-B))+1)

# C*P > A+B*P
