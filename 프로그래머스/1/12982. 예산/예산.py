def solution(d, budget):
    answer = 0
    
    while d:
        m = min(d)
        if budget < m:
            break
        budget -= m
        d.remove(m)
        answer += 1
    
    return answer
