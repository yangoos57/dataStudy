# 값
from utils import set_logging


if __name__ == "__main__":
    logger = set_logging()

    M, N = map(int, input().split(" "))
    # logger.info([M, N])

    # v = [0]
    # for i in range(1, 46):
    #     v += [i] * i

    # print(sum(v[M : N + 1]))

    i = 0
    sum_m = 0
    sum_n = 0
    while M != 0 or N != 0:
        i += 1
        v_list = []
        v_list += [i] * i

        for v in v_list:
            if M != 0:
                sum_m += v
                M -= 1

            if N != 0:
                sum_n += v
                N -= 1

    print(sum_n, sum_m)
