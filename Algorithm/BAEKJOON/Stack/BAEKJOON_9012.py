# 괄호
# https://www.acmicpc.net/problem/9012

N = int(input())

for _ in range(N):
    
    S = str(input())
    stack = []

    for s in S:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
    
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")