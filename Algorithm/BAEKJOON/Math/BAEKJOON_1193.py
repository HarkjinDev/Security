# 분수찾기
# https://www.acmicpc.net/problem/1193

# 1/1 1/2 2/1 3/1 2/2 1/3 1/4 2/3 3/2 2/4

n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line % 2 == 0:
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))
