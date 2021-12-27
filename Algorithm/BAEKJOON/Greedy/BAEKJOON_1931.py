# 회의실 배정
# https://www.acmicpc.net/problem/1931

N = int(input())

meet_list = list()

for _ in range(N):
    x, y = map(int, input().split())
    meet_list.append([x, y])

meet_list.sort(key=lambda x: x[0])
meet_list.sort(key=lambda x: x[1])

last = 0
count = 0

for x, y in meet_list:
    if x >= last:
        count += 1
        last = y

print(count)    

# 1열은 회의정보(시간시간 끝시간)
# 2~N+1은 각 N의 회의정보(시작시간 끝시간)


