from collections import deque

graph = {
    'A': ['B','C'],
    'B': ['A', 'D','E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited =set()

def bfs_iterative(start_node):
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])


#stack을 사용하여 dfs
def dfs_iterative(start_node):
    stack =[start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))

start_node ='A'
bfs_iterative(start_node)