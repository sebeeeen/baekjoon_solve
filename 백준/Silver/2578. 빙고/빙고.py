import itertools
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
rows = len(board)
cols = len(board[0])
cnt = 0

def check_bingo(board):
    bingo = 0
    # 행 검사
    for r in range(5):
        if all(board[r][c] == 0 for c in range(5)):
            bingo += 1
    # 열 검사
    for c in range(5):
        if all(board[r][c] == 0 for r in range(5)):
            bingo += 1
    # 대각선 검사
    if all(board[i][i] == 0 for i in range(5)):
        bingo += 1
    if all(board[i][4 - i] == 0 for i in range(5)):
        bingo += 1
    return bingo


for i in range(5):
    ans = sum([list(map(int, input().split()))],[])
    for num in ans :
        cnt+=1
        for k in range(rows * cols):
            if board[k // cols][k % cols] == num:
                board[k // cols][k % cols] = 0
                if check_bingo(board) >= 3 :
                    print(cnt)
                    quit()