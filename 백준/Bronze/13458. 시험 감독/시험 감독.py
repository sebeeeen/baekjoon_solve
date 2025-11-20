cnt = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

for exam_site in A:
    exam_site -= B
    if exam_site > 0 :
        if exam_site % C == 0:
            cnt += exam_site // C
        else:
            cnt += exam_site // C + 1

print(cnt)