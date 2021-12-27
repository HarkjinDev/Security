# ATM
# https://www.acmicpc.net/problem/11399

N = int(input())

x = list(map(int, input().split()))

x.sort()

result = []

for i in range(N):
    s = 0
    for j in range(i+1):
        s += x[j]
    result.append(s)

print(sum(result))

