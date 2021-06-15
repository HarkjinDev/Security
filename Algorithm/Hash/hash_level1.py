# Programmers - Hash level1
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    dic = {}
    hash_sum = 0
    for p in participant:
        dic[hash(p)] = p
        hash_sum += hash(p)
    for c in completion:
        hash_sum -= hash(c)
    answer = dic[hash_sum]
    return answer

# Test Part
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
