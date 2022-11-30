n = 13

lst = [0, 0, 1, 1, 2]

for i in range(5, n + 1):
    lst_1 = []
    for j in range(1, 5):
        val = j + lst[i - j]
        lst_1.append(val)

    k = i
    c = 0
    while k > 1:
        c += 1
        if k % 5 == 0:
            k //= 5
        elif k % 3 == 0:
            k //= 3
        elif k % 2 == 0:
            k //= 2
        else:
            k -= 1

    lst_1.append(c)
    print(i, "번째", lst_1)
    lst.append(min(lst_1))

print(lst)
