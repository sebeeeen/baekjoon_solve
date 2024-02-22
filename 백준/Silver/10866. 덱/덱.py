from collections import deque
import sys

# 덱 생성
deq = deque()

# 입력
N = int(sys.stdin.readline())

# 결과를 저장할 리스트
result = []

# 명령 처리
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        deq.appendleft(command[1])

    elif command[0] == 'push_back':
        deq.append(command[1])

    elif command[0] == 'pop_front':
        if deq:
            result.append(deq.popleft())
        else:
            result.append(-1)

    elif command[0] == 'pop_back':
        if deq:
            result.append(deq.pop())
        else:
            result.append(-1)

    elif command[0] == 'size':
        result.append(len(deq))

    elif command[0] == 'empty':
        if deq:
            result.append(0)
        else:
            result.append(1)

    elif command[0] == 'front':
        if deq:
            result.append(deq[0])
        else:
            result.append(-1)

    elif command[0] == 'back':
        if deq:
            result.append(deq[-1])
        else:
            result.append(-1)

# 결과 출력
for res in result:
    print(res)
