import sys
input = sys.stdin.readline

n = int(input())
stone = [0] * 1001

for i in range(1,n+1) :
    if i == 1 :
        stone[i] = "SK"
        continue
    if i == 2 :
        stone[i] = "CY"
        continue
    if stone[i-1] == "SK" :
        stone[i] = "CY"
    if stone[i-1] == "CY" :
        stone[i] = "SK"
    
print(stone[n])