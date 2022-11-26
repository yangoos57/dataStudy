# stack의 장점 : pop을 통해 리스트 개수를 점차 줄여나갈 수 있기 때문에 시간 단축 가능
# stack 원리를 아직 이해를 못한건가 문제를 못풀겠다.

# 정확히는 이해못했지만 현재까지 이해한 바를 기록하면
# 앞 > 뒤 인 경우 stack에 index 저장, 앞 < 뒤 인 경우 나올때까지 반복
# 앞 < 뒤 발견하면 index 역순으로 계산하며 stack 제거 앞 > 뒤 인 경우 나올때까지 반복
# stack이 점차 소멸하는 구조로 짜여있기 때문에 시간이 효율적인 것으로 보임
# for문이 다 돌면 종료
# stack_list에 idx를 넣어두고
# answer list의 값만 바꾸는 방법을 썼음
# 1929 문제에서 idx list를 on/off 기능으로 쓰면 특정 값만을 추출 할 수 있는 것과
# 원리가 같다고 보면 됨

import sys

input = sys.stdin.readline

N = int(input().rstrip())
val_list = list(map(int, input().rstrip().split()))


n = 4
val_list = [9, 5, 4, 8]


answer = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and val_list[stack[-1]] < val_list[i]:
        answer[stack.pop()] = val_list[i]

    stack.append(i)
    print(stack)

print(*answer)
