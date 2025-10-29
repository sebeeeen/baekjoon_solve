n, m = map(int, input().split())

min_package = 10**9
min_single = 10**9

for _ in range(m):
    p, s = map(int, input().split())
    if p < min_package:
        min_package = p
    if s < min_single:
        min_single = s

cost_all_single = n * min_single

cost_mix = (n // 6) * min_package + (n % 6) * min_single

cost_all_package = (n // 6 + 1) * min_package

answer = min(cost_all_single, cost_mix, cost_all_package)
print(answer)
