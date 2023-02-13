# 2875
# https://www.acmicpc.net/problem/2875


N, M, K = map(int, input().split(" "))

# 결성가능한 팀, 남은 여학생
N_a, N_b = N // 2, N % 2

# 실제 팀 생성
team_len = min(N_a, M)

M_b = M - team_len
while True:
    rest_people = N_b + M_b
    if rest_people < K:
        team_len -= 1
        N_b += 2
        M_b += 1
    else:
        break

print(team_len)
