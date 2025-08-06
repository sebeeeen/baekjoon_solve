import sys
input = sys.stdin.readline

def T(n): return n * (n + 1) // 2

n = int(input())
num = sum([list(map(int, input().split())) for _ in range(n)], [])

index = 0
while index != n:
    for i in range(1, 45):
        for j in range(1, 45):
            for k in range(1, 45):
                if num[index] == T(i) + T(j) + T(k):
                    print(1)
                    break
            else: continue
            break
        else: continue
        break
    else: print(0)
    index += 1
