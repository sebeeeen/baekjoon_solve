import sys
input = sys.stdin.readline

m = int(input())

for i in range(1, m + 1):
    i_str = str(i)
    result = i + sum(int(n) for n in i_str)
    if result == m:
        print(i)
        break
else:
    print(0)
