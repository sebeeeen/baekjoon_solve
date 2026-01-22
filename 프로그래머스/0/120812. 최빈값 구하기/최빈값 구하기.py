def solution(array):
    from collections import Counter
    num_counter = Counter(array)
    max_v, answer = 0, 0 
    
    for number in num_counter:
        if max_v < num_counter[number] :
            max_v = num_counter[number]
            answer = number
        elif max_v == num_counter[number] :
            answer = -1
            
    return answer