# 숫자의 합
# https://www.acmicpc.net/problem/11720

N = int(input())
number = str(input())

sum = 0

for i in range(N):
    sum += int(number[i])

print(sum)