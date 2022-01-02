# 회전하는 큐
# https://www.acmicpc.net/problem/1021

from collections import deque

N, M = map(int, input().split())

number = list(map(int, input().split()))

q = deque()
for j in range(1, N+1):
    q.append(j)

count = 0

for i in range(M):
    while(q):
        if q[0] == number[i]:
            q.popleft()
            break
        else:
            # index의 길이가 q의 반(중앙 기준)보다 작으면 왼쪽으로 옮기는게 최소
            if q.index(number[i]) < len(q)/2:
                while q[0] != number[i]:
                    q.rotate(-1)
                    count += 1
            else:
                # 중앙 기준ㅇ보다 크면 오른쪽으로 옮기는게 최소
                while q[0] != number[i]:
                    q.rotate(1)
                    count += 1

print(count)
