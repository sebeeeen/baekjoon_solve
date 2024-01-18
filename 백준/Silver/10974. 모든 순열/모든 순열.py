n = int(input())
arr = [0] * n

def print_num(arr, n, count):
    if count == n:
        print(*arr)
        return
    for i in range(1, n + 1): #중복된 값이 이미 배열에 있는지 확인
        if i not in arr[:count]:
            arr[count] = i
            print_num(arr, n, count + 1)

print_num(arr, n, 0)




