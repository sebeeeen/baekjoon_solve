n, s, m = map(int, input().split())
v = list(map(int, input().split()))

p = [set() for _ in range(n+1)]
p[0].add(s)   

for i in range(1, n+1):
    for prev in p[i-1]:  
        if prev + v[i-1] <= m:
            p[i].add(prev + v[i-1])
        if prev - v[i-1] >= 0:
            p[i].add(prev - v[i-1])

if p[n]:
    print(max(p[n]))
else:
    print(-1)
