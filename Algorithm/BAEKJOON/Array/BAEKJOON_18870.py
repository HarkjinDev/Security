# 좌표 압축
# https://www.acmicpc.net/problem/18870

import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

# Timeout
'''
for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue
        if X[i] > X[j]:
            count += 1
    print(count, end=" ")
'''
# set 중복
XS = sorted(list(set(X)))
dic = { XS[i] : i for i in range(len(XS))}

for i in X:
    print(dic[i], end=' ')