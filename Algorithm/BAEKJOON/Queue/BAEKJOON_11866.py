# 오세푸스 문제 0
# https://www.acmicpc.net/problem/11866

from collections import deque

N, M = map(int, input().split())

q = deque()

for i in range(1, N+1):
    q.append(i)

answer = []
count = 1

while q:
    if count == M:
        answer.append(q[0])
        q.popleft()
        count = 1
    else:
        q.rotate(-1)
        count += 1

print("<", end="")
for i in answer:
    if i == answer[-1]:
        print(i, end="")
    else:
        print(i, end=", ")
print(">", end="")
