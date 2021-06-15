# Programmers - Hash level2_1
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    
    phone_book.sort()

    for phone1, phone2 in zip(phone_book, phone_book[1:]):
        if phone2.startswith(phone1):
            return False
    return True


## Test Part
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
