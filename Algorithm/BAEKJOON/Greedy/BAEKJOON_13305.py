# 주유소
# https://www.acmicpc.net/problem/13305

N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = 0
m = cost[0]

for i in range(N-1):
    if cost[i] >= m:
        result += m * distance[i]
    else:
        m = cost[i]
        result += m * distance[i]

print(result)

# 4
# 2 3 1
# 5 2 4 1
