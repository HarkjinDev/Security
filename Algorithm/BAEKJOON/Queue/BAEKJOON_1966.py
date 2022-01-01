# 프린터 큐
# https://www.acmicpc.net/problem/1966
from collections import deque

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  imp = list(map(int, input().split()))
  
  q = deque()
  for i in imp:
    q.append(i)
  
  idx = deque()
  for i in range(0, N):
    idx.append(i)

  cnt = 0

  while q:
      if q[0] == max(q):
        cnt += 1   
        if idx[0] == M:
          print(cnt)
          break
        else:
          q.popleft()
          idx.popleft()
      else:
        # q.rotate(-1)
        q.append(q.popleft())
        idx.append(idx.popleft())
      
      
