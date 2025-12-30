def solution(nums):
    from collections import Counter
    answer = Counter(nums)
    print(answer)
    return len(answer) if (len(nums)//2) > len(answer) else (len(nums)//2)