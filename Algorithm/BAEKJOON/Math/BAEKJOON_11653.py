# 소인수분해
# https://www.acmicpc.net/problem/11653

def factorization(n):
    d = 2

    while d <= n:
        if n % d == 0:
            print(d)
            n = n // d
        else:
            d = d + 1

N = int(input())

if N == 1:
    exit
else:
    factorization(N)