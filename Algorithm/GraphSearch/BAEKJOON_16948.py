# DeathNight
# https://www.acmicpc.net/problem/16948

from sys import stdin
from collections import deque

def bfs():
    visit[r1][c1] = True
    queue.append((r1,c1))
    dx = [-2,-2,0,0,2,2]
    dy = [-1,1,-2,2,-1,1]
    
    count = 0
    while queue:
        count += 1
        for _ in range(len(queue)):
            # x, y : current
            x, y = queue.popleft()
            for i in range(6):
                # next x and y
                nx, ny = x+dx[i], y+dy[i]
                if nx == r2 and ny == c2:
                    return count
                if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx,ny))
    return -1

N = int(stdin.readline())
r1, c1, r2, c2 = map(int, stdin.readline().split())

queue = deque()
visit = [[False]*N for _ in range(N)]

print(bfs())
