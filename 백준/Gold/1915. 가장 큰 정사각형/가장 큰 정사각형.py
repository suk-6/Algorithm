Y, X = map(int, input().split())
dp = [[i for i in list(map(int, list(input())))] for _ in range(Y)]
result = 0

for i in range(Y):
    for j in range(X):
        if i > 0 and j > 0 and dp[i][j] == 1:
            dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        result = max(result, dp[i][j])

print(result ** 2)