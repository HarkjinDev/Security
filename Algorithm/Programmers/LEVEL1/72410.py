# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    
    #1
    new_id = new_id.lower()
    
    #2
    for s in new_id:
        if s.isalnum() or s in '-_.':
            answer += s
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    #4
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    #5
    if answer == '':
        answer = 'a'
    
    #6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #7
    if len(answer) < 3:
        answer = answer + answer[-1] * (3-len(answer))
    
    return answer
