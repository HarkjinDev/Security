# 상수
# https://www.acmicpc.net/problem/2908

s1, s2 = str(input()).split()

n1 = int(s1[::-1])
n2 = int(s2[::-1])

if n1 > n2:
    print(n1)
else:
    print(n2)

'''
s1 = int(reversed(s1))
s2 = int(reversed(s2))

if s1 > s2:
    print(s1)
else:
    print(s2)

print(s1, s2)
'''