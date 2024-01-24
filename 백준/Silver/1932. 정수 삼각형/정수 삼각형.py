import sys
input = sys.stdin.readline

n = int(input())
before_arr = [list(map(int, input().split())) for _ in range(n)]
after_arr = [0] * n
index =0


for i in range(n-1,0,-1) :
    for j in range(i) :
        if i == n-1 :
            left = before_arr[i][j]+before_arr[i-1][j]
            right = before_arr[i][j+1]+before_arr[i-1][j]
            after_arr[j] = max(left,right)
        if i < n-1 :
            left = before_arr[i-1][j]+after_arr[j]
            right = before_arr[i-1][j]+after_arr[j+1]
            after_arr[j] = max(left,right)
        

if n == 1 :
    print(before_arr[0][0])
else :
    print(after_arr[0])
