def solution(answers):
    person1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [0, 0, 0]
    num_count_1 = 0 
    num_count_2 = 0
    return_answer = []
    
    for question in answers:        
        if num_count_1 > 9 :
            num_count_1 = 0
        if num_count_2 > 7 :
            num_count_2 = 0
            
        if question == person1[num_count_1] :
            answer[0] +=1
        if question == person2[num_count_2] :
            answer[1] +=1
        if question == person3[num_count_1] :
            answer[2] +=1
            
        num_count_1 += 1 
        num_count_2 += 1 
        
    max_value = max(answer)
    
    for idx, element in enumerate(answer):
        if element == max_value:
            return_answer.append(idx+1)
    return return_answer