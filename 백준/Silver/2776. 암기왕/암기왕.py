import sys
input = sys.stdin.readline

T = int(input())

a = []
b = []

for j in range(T) :
    N = int(input())
    a = list(map(int, input().split()))
    M = int(input())
    b = list(map(int, input().split()))

    a.sort()

    count = False

    for i in range(M):
        low = 0
        high = N - 1
        while low <= high:
            mid = low + (high - low) // 2
            if a[mid] == b[i]:
                count = True
                break
            elif a[mid] > b[i]:
                high = mid - 1
            else:
                low = mid + 1
        if count:
            print("1")
        else:
            print("0")
        count = False
