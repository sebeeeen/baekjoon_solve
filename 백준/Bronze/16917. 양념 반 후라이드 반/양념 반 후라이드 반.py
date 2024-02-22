A, B, C, X, Y = map(int, input().split())

# 반반 치킨을 이용
half_chicken_cost = max(X, Y) * min(2 * C, A + B)

# 반반 치킨과 일반 치킨을 이용
chicken_cost = (2*C) * min(X,Y)
if X-Y >0 :
    chicken_cost += (A * (X-Y))
if Y-X >0 :
    chicken_cost += (B * (Y-X))

# 각각 구매하는 경우
full_chicken_cost = X * A + Y * B

# 두 경우 중에서 최솟값을 선택하여 출력
min_cost = min(half_chicken_cost, full_chicken_cost,chicken_cost)
print(min_cost)

