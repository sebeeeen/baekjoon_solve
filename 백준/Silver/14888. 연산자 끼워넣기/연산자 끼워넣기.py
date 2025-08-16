import itertools
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  

max_val = -int(1e10)
min_val = int(1e10)

for add in itertools.combinations(range(1, n), op[0]): 
    for minu in itertools.combinations([i for i in range(1, n) if i not in add], op[1]): 
        for mul in itertools.combinations([i for i in range(1, n) if i not in add and i not in minu], op[2]):
            for div in itertools.combinations([i for i in range(1, n) if i not in add and i not in minu and i not in mul], op[3]):  
                
                ops = {}
                for i in add:
                    ops[i] = '+'
                for i in minu:
                    ops[i] = '-'
                for i in mul:
                    ops[i] = '*'
                for i in div:
                    ops[i] = '/'
                
                result = num[0]
                for i in range(1, n):
                    op_now = ops[i]
                    if op_now == '+':
                        result += num[i]
                    elif op_now == '-':
                        result -= num[i]
                    elif op_now == '*':
                        result *= num[i]
                    elif op_now == '/':
                        if result < 0:
                            result = -(-result // num[i]) 
                        else:
                            result //= num[i]

                max_val = max(max_val, result)
                min_val = min(min_val, result)

print(max_val)
print(min_val)
