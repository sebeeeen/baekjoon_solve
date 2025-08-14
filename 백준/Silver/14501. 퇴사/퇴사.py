import sys
input = sys.stdin.readline

n = int(input())
t, p = [], []

for _ in range(n):
    t_i, p_i = map(int, input().split())
    t.append(t_i)
    p.append(p_i)

def asap(n, t, p):
    m = [0]*n
    for i in range(n):
        if m[i] == 0:
            if i + t[i] <= n:
                for date in range(i, i + t[i]):
                    m[date] = p[i] / t[i]
    return int(sum(m))

def amount(n, t, p):
    m = [0]*n
    max_profit = 0

    def dfs(day, total, m_copy):
        nonlocal max_profit
        if day >= n:
            max_profit = max(max_profit, total)
            return

        if day + t[day] <= n:
            m_new = m_copy[:]
            for i in range(day, day + t[day]):
                m_new[i] = p[day] / t[day]
            dfs(day + t[day], total + p[day], m_new)

        dfs(day + 1, total, m_copy[:])

    dfs(0, 0, m)
    return max_profit

print(max(asap(n, t, p), amount(n, t, p)))
