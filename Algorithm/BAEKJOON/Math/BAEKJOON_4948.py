# 베르트랑 공준
# https://www.acmicpc.net/problem/4948

# n, n < x < 2n

import math

def fact(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

allnumber = list(range(2, 246912))
fact_list = list()

for i in allnumber:
    if fact(i):
        fact_list.append(i)

n = int(input())

while True:
    count = 0
    if n == 0:
        break
    for i in fact_list:
        if n < i <= 2*n:
            count += 1
    
    print(count)
    n = int(input())