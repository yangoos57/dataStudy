# 값
from utils import set_logging


if __name__ == "__main__":
    logger = set_logging()

    M, N = map(int, input().split(" "))
    # logger.info([M, N])

    v = [0]
    for i in range(1, 46):
        v += [i] * i

    print(sum(v[M : N + 1]))
