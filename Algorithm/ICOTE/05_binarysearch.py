def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

'''
Input :
10 7
1 3 5 7 9 11 13 15 17 19

result : 4
'''

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

