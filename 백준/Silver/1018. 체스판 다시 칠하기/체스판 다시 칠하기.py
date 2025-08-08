import sys
input = sys.stdin.readline

n = list(map(int, input().split()))
chess = []
for _ in range(n[0]):
    chess.extend(list(input().strip()))
chess.append('\n')

def repaint(matrix, color):
    matrix = matrix[:]
    count = 0
    i = 0
    line = 0
    while matrix[i] != '\n' and line < 8:
        if i == 0 and matrix[i] != color:
            matrix[i] = color
            count += 1
        elif i < 8 and matrix[i - 1] == matrix[i]:  # 첫 줄: 좌우 비교
            matrix[i] = 'B' if matrix[i - 1] == 'W' else 'W'
            count += 1
        elif i >= 8 and matrix[i - 8] == matrix[i]:  # 이후 줄: 위쪽 비교
            matrix[i] = 'B' if matrix[i - 8] == 'W' else 'W'
            count += 1
        if i % 8 == 7:  # 매 8번째 열마다 줄 넘김
            line += 1
        i += 1
    return count

min_count = float('inf')

for row in range(n[0] - 7):
    for col in range(n[1] - 7):
        sliced = []
        for i in range(8):
            for j in range(8):
                sliced.append(chess[(row + i) * n[1] + (col + j)])
        sliced.append('\n')
        min_count = min(min_count, repaint(sliced, 'W'), repaint(sliced, 'B'))

print(min_count)
