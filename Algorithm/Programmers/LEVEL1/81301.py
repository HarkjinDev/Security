# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ''
    english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, num in enumerate(english):
        if num in s:
            s = s.replace(num, str(idx))
    
    return int(s)
