# 미로 탐색 (BFS)
# https://www.acmicpc.net/problem/2178

from sys import maxsize, stdin
from collections import deque

N, M = map(int, stdin.readline().split())
maze = [list(map(int, stdin.readline().strip())) for _ in range(N)]

queue = deque()
route = [[0]*M for _ in range(N)]
visit = [[False]*M for _ in range(N)]

queue.append((0,0))
visit[0][0] = True
route[0][0] = 1

'''
Direct x,y
dx[0] dy[1] : right
dx[1] dy[1] : left
dx[2] dy[2] : down
dx[3] dy[3] : up
'''
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == 1 and not visit[nx][ny] :
                visit[nx][ny] = True
                queue.append([nx,ny])
                route[nx][ny] = route[x][y] + 1

print(route[N-1][M-1])
