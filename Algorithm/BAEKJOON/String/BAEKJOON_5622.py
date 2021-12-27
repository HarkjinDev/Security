# 다이얼
# https://www.acmicpc.net/problem/5622

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

S = input()

result = 0

for i in range(len(S)):
    cnt = 2
    for d in dial:
        if S[i] in d:
            result += dial.index(d)+3

print(result)