import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
bacon, result = 10**9, 0   # 충분히 큰 값으로 초기화

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def bfs(start):
    visited = [-1] * (n+1)
    q = deque([start])
    visited[start] = 0  

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                q.append(nxt)

    return sum(visited[1:])

for v in range(1, n+1):
    dist_sum = bfs(v)
    if dist_sum < bacon:
        bacon = dist_sum
        result = v
    elif dist_sum == bacon and v < result:
        result = v

print(result)
