def make_team(n, m):
    cnt = 0
    while n > 1 and m > 0:
        n -= 2
        m -= 1
        cnt += 1
    return cnt

n, m, k = map(int, input().split())
max_cnt = 0

if k == 0:
    max_cnt = max(make_team(n, m), max_cnt)

for i in range(k+1):
    cal_n = n - i
    cal_m = m - (k - i)
    max_cnt = max(make_team(cal_n, cal_m), max_cnt)

print(max_cnt)
