# 블랙잭
# https://www.acmicpc.net/problem/2798

from itertools import combinations

N, M = map(int, input().split())
card = list(map(int, input().split()))

result = 0
# 1)
for c1 in range(N):
    for c2 in range(c1+1, N):
        for c3 in range(c2+1, N):
            if card[c1] + card[c2] + card[c3] > M:
                continue
            else:
                result = max(result, card[c1] + card[c2] + card[c3])

# print(result)

result = 0
# 2)
for cards in combinations(card, 3):
    if result < sum(cards) <= M:
        result = sum(cards)

print(result)

