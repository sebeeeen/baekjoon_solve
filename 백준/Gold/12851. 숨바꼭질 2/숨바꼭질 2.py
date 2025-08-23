import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False] * 100001
time = [0] * 100001   
count = [0] * 100001 

def bfs(start):
    q = deque([start])
    visited[start] = True
    count[start] = 1

    while q:
        x = q.popleft()
        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx <= 100000:
                if not visited[nx]:
                    visited[nx] = True
                    time[nx] = time[x] + 1
                    count[nx] = count[x]
                    q.append(nx)
                elif time[nx] == time[x] + 1:
                    count[nx] += count[x]

bfs(n)
print(time[m])   
print(count[m]) 
