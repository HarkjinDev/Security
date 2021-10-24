import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result

def heapsort_reverse(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result    

result1 = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
result2 = heapsort_reverse([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result1)
print(result2)
