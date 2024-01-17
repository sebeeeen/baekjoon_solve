import sys
input = sys.stdin.readline

s = input()
output = ""
print_bool = False

for i in range(len(s)) :
    output +=s[i]
    if s[i] == ' ' and print_bool==False:
        for j in range(-2,-len(output)-1,-1) :
            print(output[j],end="")
        output = ""
        if s[i+1] != " ":
            print(" ",end="")
    if s[i] =="\n" or s[i]=='<':
        for j in range(-2,-len(output)-1,-1) :
            print(output[j],end="")
    if s[i] == '<':
        print_bool = True
    if print_bool == True :
        print(s[i], end="")
    if s[i] == '>':
        print_bool = False
        output = ""
    