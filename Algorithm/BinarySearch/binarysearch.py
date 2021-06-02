import sys

def binary_search(arr, target, left=None, right=None):

    left, right = 0, len(arr) - 1

    while left <= right:

        mid = (left+right) // 2

        if arr[mid] > target:
            right = mid -1
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
            
    return -1

def binary_search_recursion(arr, target, left=None, right=None):

    left, right = left or 0, right or len(arr) - 1

    if left > right:
        return -1

    mid = (left+right) // 2

    if arr[mid] > target:
        return binary_search_recursion(arr, target, left, mid-1)
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursion(arr, target, mid+1, right)


sys.setrecursionlimit(10000)

# This is test part
print("binary_search : ", binary_search(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P"], "G"))
print("binary_search_recursion : ", binary_search_recursion(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P"], "G"))
