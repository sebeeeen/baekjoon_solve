import sys
input = sys.stdin.readline

n = int(input())
s = [0] * 21
input_values = [0] * 2

for _ in range (n) :
    input_values = input().split()
    op = input_values[0]
    if op != "all" and op != "empty" :
        value = int(input_values[1])
    if op == "add" and s[value]==0:
        s[value] = 1
    if op == "remove" and s[value]!=0 :
        s[value] = 0
    if op == "check" :
        if s[value] == 0 :
            print("0")
        else :
            print("1")
    if op == "toggle" :
        if s[value] == 0 :
            s[value] = 1
        elif s[value] == 1 :
            s[value] = 0
    if op == "all" :
        for i in range(1,21) :
            s[i] = 1
    if op == "empty" :
        for i in range(1,21) :
            s[i] = 0
    