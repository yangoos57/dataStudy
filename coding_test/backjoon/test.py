from collections import deque

# 순번이 가장 앞이고 우선순위가 가장 높을 때 출력 

# 그러지 않을 땐 가장 마지막으로 옮김

# 출력 된 경우 max 값을 다시 찾고 idx 한 칸 앞으로 조정한 뒤 위 절차를 반복


tc=int(input())

for _ in range(tc):
    N,idx=map(int,input().split())
    input_data=list(map(int,input().split()))


    queue = deque(input_data)

    # max 값
    max_var = max(queue)

    output = 0 # 출력된 순서

    while len(queue) != 0 :
        
        if queue[0] != max_var :
            if idx == 0 :
                N = len(queue)
                idx = N -(idx+1)
            else :
                idx -= 1
            var = queue.popleft()
            queue.append(var)
            
        else :
            queue.popleft()
            output += 1     

            if idx == 0 :
                break
            else:
                idx -= 1
                max_var = max(queue)
    print(output)