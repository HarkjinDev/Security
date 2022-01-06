# 덩치
# https://www.acmicpc.net/problem/7568

N = int(input())

people = []

for _ in range(N):
    [weight, tall] = map(int, input().split())
    people.append([weight, tall])

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
