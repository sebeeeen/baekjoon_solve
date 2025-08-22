import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
visited = [False] * 100001

def bfs(start) :
    q = deque([(start,0)])
    visited[start] = True
    while q:
        x,t = q.popleft()
        if x == m :
            return t
        for nx in (x-1,x+1,x*2) :
            if 0 <= nx <= 100000 and not visited[nx] :
                visited[nx] = True
                q.append((nx,t+1))

print(bfs(n))

