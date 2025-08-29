import sys
input = sys.stdin.readline

n = int(input())
t, p = [], []
dp = [0] * (n+2)

for _ in range(n):
    t_i, p_i = map(int, input().split())
    t.append(t_i)
    p.append(p_i)

for i in range(n-1, -1, -1):
    if i+t[i] <= n:
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])
    else:
        dp[i] = dp[i+1]

print(dp[0])