from collections import deque

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

print(bfs(graph, 'A'))


visited = []
def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)

dfs('A')

print(visited)