import sys

n = int(sys.stdin.readline())
input = [sys.stdin.readline().strip() for i in range(n)]

st1 = []
st2 = []
for var in input:
    var = var.split()
    if var[0] == "push":
        st2.append(int(var[1]))
    elif var[0] == "pop":
        if st2:
            print(st2.pop(0))
        else:
            print(-1)
    elif var[0] == "size":
        print(len(st2))
    elif var[0] == "empty":
        if st2:
            print(0)
        else:
            print(1)
    elif var[0] == "front":
        if st2:
            print(st2[0])
        else:
            print(-1)
    elif var[0] == "back":
        if st2:
            print(st2[-1])
        else:
            print(-1)
