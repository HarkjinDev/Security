# 나이순 정렬
# https://www.acmicpc.net/problem/10814

n = int(input())
x = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    x.append((age, name))

x.sort(key=lambda x : x[0])

for i in x:
    print(i[0], i[1])
