import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())
cnt = 0

def dfs(graph, rows, cols, n, m):
    if rows < 0 or rows >= n or cols < 0 or cols >= m:   
        return
    if graph[rows][cols] == False:  
        return
    
    graph[rows][cols] = False  
    
    dfs(graph, rows+1, cols, n, m)
    dfs(graph, rows-1, cols, n, m)
    dfs(graph, rows, cols+1, n, m)
    dfs(graph, rows, cols-1, n, m)


while cnt != t:
    n, m, k = map(int, input().split())  
    graph = [[False] * n for _ in range(m)]  
    
    for _ in range(k):
        col, row = map(int, input().split())  
        graph[row][col] = True  
    
    answer = 0
    for rows in range(m):
        for cols in range(n):
            if graph[rows][cols] == True:
                dfs(graph, rows, cols, m, n)
                answer += 1
    
    print(answer)
    cnt += 1
