from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_vaule):
    right_index = bisect_right(array, right_vaule)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

'''
input:
7 2
1 1 2 2 2 2 3
result : 4
'''

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x , x)

if count == 0:
    print(-1)
else:
    print(count)