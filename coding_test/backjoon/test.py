# 11726은 쉽게 풀고 11727은 풀지 못한 이유
# 도형의 반복되는 패턴을 도형 패턴으로 이해하지 않고 수열로 접근했기 때문으로 생각

# 짝수와 홀수의 다른 패턴을 식별해서 구했다. 예제는 맞았는데 실제에서는 계속 틀렸다.
# 초반 8개 값을 가지고 패턴을 찾으려고 해서 그런 것 같다.

# 실제로 n 55 이후부터 에러가 발생한다.


dp = [1] * 1001
dp[2] = 3
for n in range(3, 1001):
    if n % 2 == 0:
        dp[n] = int(dp[n - 2] + 2 ** (n - 1))
    else:
        dp[n] = int(dp[n - 2] + 4 ** ((n - 1) / 2))

answer = [n % 10007 for n in dp]
