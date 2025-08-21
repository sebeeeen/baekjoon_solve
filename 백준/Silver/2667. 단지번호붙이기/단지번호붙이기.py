import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())
graph = []
answer = 0
result = []

def dfs(row, col):
    if row < 0 or row >= t or col < 0 or col >= t:
        return 0
    if graph[row][col] == 0:
        return 0

    graph[row][col] = 0
    cnt = 1

    cnt += dfs(row+1, col)
    cnt += dfs(row-1, col)
    cnt += dfs(row, col+1)
    cnt += dfs(row, col-1)

    return cnt

for _ in range(t):
    graph.append(list(map(int, input().strip())))

for i in range(t):
    for j in range(t):
        if graph[i][j] == 1:
            result.append(dfs(i, j))
            answer += 1

print(answer)
for r in sorted(result):
    print(r)
