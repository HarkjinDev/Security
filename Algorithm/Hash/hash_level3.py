# Programmers - Hash level3
# https://programmers.co.kr/learn/courses/30/lessons/42579

from collections import *

def solution(clothes):

    dic = defaultdict(list)
    answer = 1

    for item, category in clothes:
        dic[category].append(item)

    for i in dic.keys():
        answer *= len(dic[i]) + 1

    answer -= 1

    return answer

# Test Part
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
