import itertools
import sys
input = sys.stdin.readline

n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]
index = list(range(n)) 
result = 1e9 

for comb in itertools.combinations(index, n // 2):
    start = comb
    link = list(set(index) - set(comb))

    s = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            s += b[start[i]][start[j]] + b[start[j]][start[i]]

    l = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            l += b[link[i]][link[j]] + b[link[j]][link[i]]

    result = min(result, abs(s - l))

print(result)
