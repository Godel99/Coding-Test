def solution(n, money):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in money:
        for x in range(coin, n+1):
            dp[x] = (dp[x] + dp[x-coin]) % MOD
    
    return dp[n]