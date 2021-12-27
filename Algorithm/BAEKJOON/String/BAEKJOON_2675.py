# 문자열 반복
# https://www.acmicpc.net/problem/2675

T = int(input())

for i in range(T):
    num, s = input().split()
    num = int(num)
    s = str(s)
    for i in range(len(s)):
        print(num*s[i],end='')
    print()
