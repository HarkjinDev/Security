def DFS_List(graph, root):
    visit = list()
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(graph[node]))

    return visit

def DFS_Dict(graph, root):
    # visit's list = O(n), dict = O(1)
    visit = dict()
    stack = list()

    stack.append(root)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            stack.extend(reversed(graph[node]))

    return list(visit.keys())

# The visit list
def DFS_Recursive(graph, root, visit=[]):

    visit.append(root)

    for node in graph[root]:
        if node not in visit:
            DFS_Recursive(graph, node, visit)

    return visit

# The visit dict
def DFS_Recursive2(graph, root, visit={}):
    
    visit[root] = True

    for node in graph[root]:
        if node not in visit:
            DFS_Recursive2(graph, node, visit)

    return list(visit.keys())

# Graph
graph_list = {
'A': ['B'],
'B': ['A', 'C', 'H'],
'C': ['B', 'D'],
'D': ['C', 'E', 'G'],
'E': ['D', 'F'],
'F': ['E'],
'G': ['C'],
'H': ['B', 'I', 'J', 'M'],
'I': ['H'],
'J': ['H', 'K'],
'K': ['J', 'L'],
'L': ['K'],
'M': ['H']
}

root_node = "A"

# Test Part
print(DFS_List(graph_list, root_node))
print(DFS_Dict(graph_list, root_node))
print(DFS_Recursive(graph_list, root_node))
print(DFS_Recursive2(graph_list, root_node))
