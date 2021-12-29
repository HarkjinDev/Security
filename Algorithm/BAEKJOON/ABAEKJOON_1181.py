# 단어 정렬
# https://www.acmicpc.net/problem/1181

N = int(input())

array = []

for i in range(N):
    array.append(input())

array = list(set(array))

array.sort()
array.sort(key=len)

for s in array:
    print(s)
