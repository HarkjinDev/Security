# 오큰수
# https://www.acmicpc.net/problem/17298

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))

stack = []

for i in range(N):
    while(stack):
        if A[i] > A[stack[-1]]:
            A[stack.pop()] = A[i]
        else:
            stack.append(i)
            break
    
    if not stack:
        stack.append(i)
for i in stack:
    A[i] = -1

print(*A)
