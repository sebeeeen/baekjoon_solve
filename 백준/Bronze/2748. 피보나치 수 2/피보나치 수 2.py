n = int(input())
cnt,fn1 = 2, 0
fn2 = 1

def dp(n,fn1,fn2, cnt):
    tmp = 0
    if cnt <=n :
        cnt +=1
        tmp = fn1
        fn1 = fn2
        fn2 = fn2 + tmp
        return dp(n,fn1, fn2, cnt)
    else : return(fn2)


print(dp(n,fn1,fn2, cnt))