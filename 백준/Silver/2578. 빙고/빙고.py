import itertools
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
rows = len(board)
cols = len(board[0])
cnt = 0

def check_bingo(board) :
    bingo = [0] * 12
    for i in range(5) :
        if board[0][i] == 0 : bingo[0] +=1
        if board[1][i] == 0 : bingo[1] +=1
        if board[2][i] == 0 : bingo[2] +=1
        if board[3][i] == 0 : bingo[3] +=1
        if board[4][i] == 0 : bingo[4] +=1
        if board[i][0] == 0 : bingo[5] +=1
        if board[i][1] == 0 : bingo[6] +=1
        if board[i][2] == 0 : bingo[7] +=1
        if board[i][3] == 0 : bingo[8] +=1
        if board[i][4] == 0 : bingo[9] +=1
        if board[i][4-i] == 0 : bingo[10] +=1
        if board[i][i] == 0 : bingo[11] +=1
    return bingo.count(5)


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