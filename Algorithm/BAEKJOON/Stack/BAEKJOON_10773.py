# 제로
# https://www.acmicpc.net/problem/10773

stack = []

N = int(input())

for _ in range(N):
    a = int(input())
    
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

result = 0

for i in stack:
    result += i

print(result)
