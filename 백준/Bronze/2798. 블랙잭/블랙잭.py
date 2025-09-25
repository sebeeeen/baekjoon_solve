import itertools

n, m = map(int, input().split())
num = list(map(int, input().split()))

near = 300000
plus = 1

for i in itertools.combinations(num, 3):
    if m - sum(i) >= 0 :
        near = min(m - sum(i), near)

print(m -near)