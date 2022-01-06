# 분해합
# https://www.acmicpc.net/problem/2231

N = int(input())

for i in range(1, N+1):
    n = list(map(int, str(i)))
    result = i + sum(n)

    if result == N:
        print(i)
        break

    if i == N:
        print(0)