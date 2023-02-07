# 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    left = 0
    right = max(times) * n
    while left<=right : 
        middle = (left + right) // 2 
        
        # 시간이 주어졌을 때 개별 심사관이 최대 몇명을 처리할 수 있는지
        # 만약 처리해야하는 것보다 많이 처리하면 시간 줄여야함.
        # 처리 해야하는 것보다 적게 처리하면 시간 늘려야함.
        people = 0
        for i in times :
            x = middle//i
            people += x
            if people >= n :
                break
            
        print(left,middle,right,people)
        if people < n : 
            left = middle + 1
        else : 
            right = middle - 1
            answer = middle
    return answer

n = 6 
times = [7,10]
print(solution(n,times))