from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
Class = [list(map(int, input().split())) for _ in range(n)]
result = [set() for _ in range(n)]  

for i in range(len(Class[0])):
    col = [row[i] for row in Class]
    cnt = Counter(col)
    if len(cnt) != n :
        for key, value in cnt.items():
            if value != 1 :
                indices = [i for i, v in enumerate(col) if v == key]
                for index in indices:
                    result[index].update(indices)  
                    result[index].discard(index)   

result = [len(s) for s in result]
print(result.index(max(result)) + 1)