# 크로아티아 알판벳
# acmicpc.net/problem/2941

alpha = [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
S = input()

count = 0

for i in alpha:
    if i in S:
        S = S.replace(i," ")

print(len(S))