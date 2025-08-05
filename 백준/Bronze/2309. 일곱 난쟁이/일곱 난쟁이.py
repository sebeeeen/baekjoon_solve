import sys
input = sys.stdin.readline

n = sum([list(map(int, input().split())) for _ in range(9)], [])
all = sum(n)

for i in range(9) :
    for j in range(9):
        r1, r2 = n[i], n[j]
        if i == j :
            break
        if (all - (r1+r2)) == 100: 
            n.remove(r1)
            n.remove(r2)
            print(*sorted(n), sep='\n')
            quit()