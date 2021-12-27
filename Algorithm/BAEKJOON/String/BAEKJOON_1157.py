# https://www.acmicpc.net/problem/1157

S = input().upper()
single = list(set(S))
cnt = []

for s in single:
    count = S.count(s)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(single[(cnt.index(max(cnt)))])
