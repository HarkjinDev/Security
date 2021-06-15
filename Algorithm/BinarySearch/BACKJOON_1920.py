# BACKJOON 1920 - Binarysearch
# https://www.acmicpc.net/problem/1920

import sys

def binarysearch(arr,target,left,right):
    if left > right:
        return False
    mid = (left+right) // 2
    if arr[mid] > target:
        return binarysearch(arr,target,left,mid-1)
    elif arr[mid] < target:
        return binarysearch(arr,target,mid+1,right)
    else:  # arr[mid]==target
        return True

N=int(input())
A=list(map(int,input().split()))
M=int(input())
m=list(map(int,input().split()))

A = sorted(A)

for i in m:
    if binarysearch(A,i, 0, N-1):
        print(1)
    else:
        print(0)
