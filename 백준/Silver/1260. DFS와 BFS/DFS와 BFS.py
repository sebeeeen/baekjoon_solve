import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m) :
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for nxt in sorted(graph[v]) :
        if not visited[nxt] :
            dfs(graph, nxt, visited)

def bfs(graph, start) :
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True

    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for nxt in sorted(graph[v]) :
            if not visited[nxt] :
                visited[nxt] = True
                queue.append(nxt)
            


dfs(graph, v, visited)
print()
bfs(graph, v)
print()
