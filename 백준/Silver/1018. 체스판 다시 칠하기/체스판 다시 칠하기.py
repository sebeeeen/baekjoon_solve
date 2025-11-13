n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

def check(row, col):
    cnt = 0  # 시작을 B로 가정한 경우의 mismatch 수

    for i in range(8):
        for j in range(8):
            expected = 'B' if (i + j) % 2 == 0 else 'W'
            if board[row + i][col + j] != expected:
                cnt += 1

    # W 시작 패턴 mismatch 수는 64 - cnt
    return min(cnt, 64 - cnt)

answer = 1e9

for r in range(n - 7):
    for c in range(m - 7):
        answer = min(answer, check(r, c))

print(answer)
