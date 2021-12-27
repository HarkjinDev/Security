# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

# abcdefghijklmnopqrstuvwxyz : 26
# print(ord('a')) 97
# print(ord('z')) 122

S = str(input())

array = [-1 for i in range(26)]

S_array = list()

for i in range(len(S)):
    S_array.append(ord(S[i]) - 97)

count = 0

for s in S_array:
    if array[s] == -1 :
        array[s] = count
    count += 1

for i in array :
    print(i, end=" ")