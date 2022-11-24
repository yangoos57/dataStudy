# 배울점
# 일단 패턴을 찾고 구현하는게 중요한 듯
# 일일히 구해보면서 어떤 패턴 있는지를 찾아봤음.
# 그리고 앞으로 원으로 stack 문제는 수열 -1 이라고 생각해야할듯!
import sys

# n = int(sys.stdin.readline())
# input_data = [sys.stdin.readline().strip() for i in range(n)]
# input_data = list(sys.stdin.readline().rstrip())
input_data = list(map(int, input().split()))
N = int(input_data[0])
K = int(input_data[1])

st1 = list(range(1, N + 1))
st2 = []

var = 0
for _ in range(N):
    var += K - 1
    if len(st1) <= (var):
        var = (var) % len(st1)
        st2.append(st1.pop(var))
    else:
        st2.append(st1.pop(var))

end = " ".join(map(str, st2))
print("<" + end + ">")

## 또는


input_data = list(map(int, input().split()))
N = int(input_data[0])
t = int(input_data[1])


a = list(range(1, N + 1))
answer = []
idx = 0
cur = 1

while cur <= N:
    len_a = len(a)
    idx += t - 1

    # 원 크기보다 idx가 클 경우 원 크기로 나워 idx를 초기화 해야함
    if idx >= len_a:
        idx = idx % len_a

    answer.append(a.pop(idx))

    cur += 1

answer_str = ", ".join(map(str, answer))

print("<" + answer_str + ">")
