import sys

# input_data = list(sys.stdin.readline().rstrip())
# input_data = list(map(int, input().split()))
# N = int(input_data[0])
# K = int(input_data[1])

# var = sys.stdin.readline().rstrip()
n = int(input())
new_a = list(map(int, input().split()))

max_var = 0
left_var = 0
answer = []
for i in range(len(new_a)):
    new_var = new_a[i]
    q = new_a[i + 1 :]

    if new_var == max(new_a) or not q:
        answer.append(-1)

    elif new_var > left_var:
        left_val = new_var
        for j in q:
            if new_var < j:
                max_var = j
                answer.append(j)
                break

    elif new_var < left_var:
        answer.append(max_var)
print(answer)
ans = list(map(str, answer))
ans = " ".join(ans)
print(ans)
