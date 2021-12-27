# 소트인사이드
# https://www.acmicpc.net/problem/1427

import sys

N = str(sys.stdin.readline())

array = list()

for i in range(len(N)-1):
    array.append(N[i])

array.sort(reverse=True)

for i in range(len(N)-1):
    print(array[i], end="")
