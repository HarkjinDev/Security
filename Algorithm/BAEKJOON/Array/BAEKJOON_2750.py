# 수 정렬하기
# https://www.acmicpc.net/problem/2750

N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(input()))

# numbers.sort(reverse=True)
numbers.sort()

for i in range(N):
    print(numbers[i])
