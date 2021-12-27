# 수 정렬하기2
# https://www.acmicpc.net/problem/11651

import sys

N = int(sys.stdin.readline())
array = []

for _ in range(N):
    [a, b] = map(int, input().split())
    array.append([b, a])

array.sort()

for i in range(N):
    print(array[i][1], array[i][0])