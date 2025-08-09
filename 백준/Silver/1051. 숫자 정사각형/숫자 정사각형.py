import sys
input = sys.stdin.readline

n,m = map(int, input().split())
box = []
result = 0

for _ in range(n):
    row = list(map(int, input().strip()))
    box.append(row)

num = list(set(sum(box, [])))

def square(matrix, num, n, m):
    result = 0
    for row in range(n):
        start = []     
        end = 0
        for col in range(m):
            if matrix[row][col] == num:
                if result < 1:
                    result = 1
                    
                end = col
                for s in start:
                    side = end - s     
                    if side >= 1 and row + side < n:
                        if (matrix[row][s] == num and
                            matrix[row][end] == num and
                            matrix[row + side][s] == num and
                            matrix[row + side][end] == num):
                            area = (side + 1) ** 2
                            if area > result:
                                result = area

                start.append(col)
    return result

for check_num in num:
    result = max(result, square(box, check_num, n, m))

print(result)
