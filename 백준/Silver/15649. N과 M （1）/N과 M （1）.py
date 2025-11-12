from itertools import permutations


n, m = map(int,input().split())
print(*[' '.join(map(str, p)) for p in permutations(range(1, n + 1), m)], sep='\n')