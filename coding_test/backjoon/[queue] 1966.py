from collections import deque

# 이 문제에서 배울 점
# pop(0)또는 insert(0, x)은 O(N)이라서 비효율적임

# queue 문제에 연산속도가 중요하다면 deque를 써야한다.
# popleft(), appendleft()는 O(1)이다.

# https://www.daleseo.com/python-queue/ 

# 



# 내가 푼 방식

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
        
        if queue[0] == max_var :
            queue.popleft()
            output += 1     

            if idx == 0 :
                break
            else:
                idx -= 1
                max_var = max(queue)
        else : 
            if idx == 0 :
                N = len(queue)
                idx = N -(idx+1)
            else :
                idx -= 1
            var = queue.popleft()
            queue.append(var)
    print(output)



### 이상적인 정답

# 특정 값의 변화를 찾고 싶을땐 [0,0,0,1,0]과 같이 특정 값의 변동을 추적할 수 있는 idx 리스트를 만들어서
# 
# 변동사항을 함께 추적하자!


input_data = [1,1,9,1,1,1]
N = len(input_data)
M = 0

idx_list = [0] * N
idx_list[M] = 1


output = 0 # 출력 횟수

while len(input_data) != 0 :
    max_int = max(input_data) 

    if max_int == input_data[0] : # max 값과 1번째 출력 순서가 같을 경우
        output += 1 # 출력 횟수 업데이트

        if idx_list[0] == 1 : # 우리가 찾는 값인 경우 종료
            print(output)
            break

        else : # 우리가 찾지 않는 값인 경우 제거하고 지속 진행
            input_data.pop(0)
            idx_list.pop(0)

    else : # max값과 1번째 출력 순서가 다를 경우 뒤로 밀려나는 것 구현
        input_data.append(input_data.pop(0))
        idx_list.append(idx_list.pop(0))