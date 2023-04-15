def solution(land):
    LENGTH = len(land)
    dp = [[0] * 4 for i in range(LENGTH)]
    dp[0] = land[0]
    for i in range(1,LENGTH):
        for j in range(4):
            sum_of_before  = 0
            for k in range(4):
                if j != k:
                    sum_of_before = max(sum_of_before, dp[i-1][k])
            dp[i][j] = land[i][j] + sum_of_before
    return max(dp[-1])