# 카드2
# https://www.acmicpc.net/problem/2164

from collections import deque

N = int(input())

queue = deque()

for i in range(1, N+1):
    queue.append(i)

while(len(queue) > 1):
    queue.popleft()
    queue.rotate(-1)

print(*queue)