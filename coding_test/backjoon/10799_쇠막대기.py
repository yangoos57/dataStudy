import sys

# n = int(sys.stdin.readline())
# input_data = [sys.stdin.readline().strip() for i in range(n)]
# input_data = list(sys.stdin.readline().rstrip())
# input_data = list(map(int, input().split()))
# N = int(input_data[0])
# K = int(input_data[1])

var = sys.stdin.readline().rstrip()
st1 = []
answer = 0
c_previous = 0
num_lazor = 0
total = 0
for num, c in enumerate(var):
    if c == "(":
        st1.append(c)
        c_previous = "("
    elif c == ")":
        st1.pop()
        total += 1
        if c_previous == "(":
            # print(num,len(st1))
            num_lazor += 1
            answer += len(st1)
        c_previous = ")"

print(answer - num_lazor + total)
