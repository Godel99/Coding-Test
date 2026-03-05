import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from math import inf

def main():
    n = int(input())
    m = int(input())
    dp = [[inf]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1): dp[i][i] = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        dp[u][v] = min(dp[u][v], w)
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    for i in range(1, n+1):
        ans = []
        for j in range(1, n+1): 
            if dp[i][j] == inf: ans.append(0)
            else: ans.append(dp[i][j])
        print(*ans)
    return 0
if __name__ == '__main__':
    main()