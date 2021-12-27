# 벌집
# https://www.acmicpc.net/problem/2292

n = int(input())

hex = 1
count = 1

while n > hex:
    hex += 6 * count
    count += 1

print(count)
