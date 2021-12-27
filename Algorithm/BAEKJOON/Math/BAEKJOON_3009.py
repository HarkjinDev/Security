# 네 번째 점
# https://www.acmicpc.net/problem/3009

x, y = list(), list()

for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(3):
    if x.count(x[i]) == 1:
        x4 = x[i]
    if y.count(y[i]) == 1:
        y4 = y[i]

print(x4, y4)

# max+min = max+min
