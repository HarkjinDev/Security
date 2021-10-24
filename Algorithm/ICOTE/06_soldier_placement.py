# 가장 긴 증가하는 부분 수열(LIS) 문제 유형

'''
input :
7
15 11 4 8 5 2 4

result : 2
'''

n = int(input())
array = list(map(int, input().split()))

array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max((dp[i], dp[j] + 1))

print(n - max(dp))

