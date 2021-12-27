# 동전 0
# https://www.acmicpc.net/problem/11047

N, WON = map(int, input().split())
coin = list()

for _ in range(N):
    coin.append(int(input()))

coin.reverse()

count = 0

for c in coin:
    if WON < 0:
        break
    if c > WON:
        continue
    else:
        count += WON // c
        WON %= c

print(count)
