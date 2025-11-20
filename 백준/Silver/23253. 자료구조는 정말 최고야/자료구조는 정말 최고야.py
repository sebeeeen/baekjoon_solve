N, M = map(int,input().split())
flag = True

for _ in range(M):
    dump_num = int(input())
    dump = list(map(int,input().split()))
    dump_sorted = list(reversed(sorted(dump)))
    if dump != dump_sorted:
        flag = False
        break
    
print("Yes" if flag else "No")