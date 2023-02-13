# 10610
# https://www.acmicpc.net/problem/10610

# 배울점
# 문제 의미 파악이 무엇보다 중요한 것 같다.
# 내가 이해한 문제는 주어진 숫자를 조합해 최대 30의 배수를 출력하는 문제인 줄 알았다.
# 98110의 경우 9810이 최대 30의 배수이다.

# 하지만 실제 문제는 주어진 숫자가 30의 배수인지를 확인하고 맞다면 최대값을 산출하는 문제였다.

# 이렇게 생각한 이유는 숫자들을 섞는다는게 '조합해'라고 이해했기 때문이다.

var = str(input())

a_0 = []
a_1 = []
a_2 = []
a_3 = []

var = list(var)
var.sort(reverse=True)

if var[-1] != "0":
    print(-1)
else:
    sum_a_1 = 0
    sum_a_2 = 0
    for v in var:
        v = int(v)
        if v == 0:
            a_0.append(str(0))
        else:
            x = v % 3
            if x == 0:
                a_3.append(str(v))
            elif x == 1:
                a_1.append(str(v))
                sum_a_1 += v
            elif x == 2:
                a_2.append(str(v))
                sum_a_2 += v

    if (sum_a_1 + sum_a_2) % 3 == 1:
        a_1.pop()
    elif (sum_a_1 + sum_a_2) % 3 == 2:
        a_2.pop()

    concat_num = a_3 + a_2 + a_1 + a_0
    print(concat_num)

    last_check = 0
    for i in concat_num:
        last_check += int(i)

    if last_check % 3 == 0:
        concat_num.sort(reverse=True)
        print("".join(concat_num))
    else:
        print(-1)
