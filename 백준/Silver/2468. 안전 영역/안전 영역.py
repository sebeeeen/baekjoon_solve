import sys
sys.setrecursionlimit(10**7)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def check(water, graph):
    dfs_graph = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if graph[x][y] != 0 and graph[x][y] <= water:
                graph[x][y] = 0
            if graph[x][y] > 0:
                dfs_graph[x][y] = 1

    return dfs_graph


def dfs(x, y, dfs_graph):
    dfs_graph[x][y] = 0  

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and dfs_graph[nx][ny] == 1:
            dfs(nx, ny, dfs_graph)


max_height = max(map(max, graph))
answer = 0

for water in range(0, max_height + 1):
    dfs_graph = check(water, graph)   
    cnt = 0
    for j in range(n):
        for k in range(n):
            if dfs_graph[j][k] == 1:
                dfs(j, k, dfs_graph)
                cnt += 1

    answer = max(answer, cnt)

print(answer)
