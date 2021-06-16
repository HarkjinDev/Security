from collections import deque

def BFS(graph, root):
    visit = list()
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

def BFS2(graph, root):
    # list = O(n), dict = O(1)
    visit = dict()
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit[node] = True
            queue.extend(graph[node])
    return list(visit.keys())

# Graph
graph_list = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

root_node = "A"

# Test Part
print(BFS(graph_list, root_node))
print(BFS2(graph_list, root_node))
