import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    MOD = 1_000_000_007
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = [[0]*5 for _ in range(n+2)]
        dp[1][0] = 1
        dp[2][0] = 3
        dp[2][1] = 1
        dp[2][2] = 1
        dp[2][3] = 1
        dp[2][4] = 1
        for i in range(3, n+2):
            dp[i][0] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2]+dp[i-1][3]+dp[i-1][4])%MOD
            dp[i][1] = (dp[i-1][0]+dp[i-1][1])%MOD
            dp[i][2] = (dp[i-1][0]+dp[i-1][2])%MOD
            dp[i][3] = (dp[i-1][2]+dp[i-1][3])%MOD
            dp[i][4] = (dp[i-1][1]+dp[i-1][4])%MOD
        print((dp[n][0]+dp[n][1]+dp[n][2])%MOD)
    return 0
if __name__ == '__main__':
    sys.exit(main())