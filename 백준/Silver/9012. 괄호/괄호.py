n = int(input())
result = [0] * n

for num in range(n):
    left, right = 0, 0
    bracket = str(input())
    for element in bracket :
        if right > left :
            result[num] = "NO"
            break
        if element == ')':
            right +=1
        elif element == '(':
            left +=1
    if right == left :
        result[num] = "YES"
    else : 
        result[num] = "NO"

[print(result[_]) for _ in range(n)]
