import sys
input = sys.stdin.readline

def T(n):
    return n * (n + 1) // 2

tri_nums = [T(i) for i in range(1, 45)] 

n = int(input())
nums = sum([list(map(int, input().split())) for _ in range(n)], [])

for x in nums:
    found = any(x == a + b + c for a in tri_nums for b in tri_nums for c in tri_nums)
    print(1 if found else 0)
