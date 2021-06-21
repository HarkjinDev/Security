# DFS and BFS
# https://www.acmicpc.net/problem/1260

from sys import stdin

def dfs(V):
    print(V, end=' ')
    visit[V] = 1
    for i in range(1,N+1):
        if visit[i] == 0 and stack[V][i] == 1:
            dfs(i)

def bfs(V):
    queue = [V]
    visit[V] = 0
    while (queue):
        V = queue[0]
        print(V, end=' ')
        del queue[0]
        for i in range(1, N+1):
            if visit[i] == 1 and stack[V][i] == 1:
                queue.append(i)
                visit[i] = 0

# N = node
# M = Metrix
# V = start visit node number

N, M, V = map(int, stdin.readline().split())
stack = [[0]*(N+1)for i in range(N+1)]
visit = [0 for i in range(N+1)]
for i in range(M):
    x, y = map(int, stdin.readline().split())
    stack[x][y] = 1
    stack[y][x] = 1

dfs(V)
print()
bfs(V)
