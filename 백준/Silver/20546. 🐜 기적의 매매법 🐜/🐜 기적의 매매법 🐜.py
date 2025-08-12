import sys
input = sys.stdin.readline

m = int(input())
stock = sum([list(map(int, input().split()))], [])

def bnp(arr, money) :
    result = 0
    for i in range(14) :
        if money >= arr[i] :
            result = money//arr[i]
            money -= result*arr[i]
    return money + result*arr[13]
        
def timing(arr, money) :
    result = 0
    plus_count = 0
    minus_count = 0
    for i in range(14) :
        if i != 0 and  arr[i]>arr[i-1] : 
            plus_count +=1
            if minus_count !=0 : minus_count=0
            if plus_count >= 3 : 
                money += result*arr[i]
                result = 0
        elif i != 0 and  arr[i]<=arr[i-1] : 
            minus_count +=1
            if plus_count !=0 : plus_count=0
            if minus_count >= 3 : 
                result += money//arr[i]
                money -= (money//arr[i])*arr[i]
    return money + result*arr[13]

if bnp(stock,m) > timing(stock,m): print("BNP")
elif bnp(stock,m) < timing(stock,m): print("TIMING")
elif bnp(stock,m) == timing(stock,m): print("SAMESAME")
