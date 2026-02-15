import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    a = input(); n = len(a)
    b = input(); m = len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1]+1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    ans = []
    while n and m:
        if a[n-1] == b[m-1]:
            ans.append(a[n-1])
            n -= 1
            m -= 1
        elif dp[n-1][m] > dp[n][m-1]: n -= 1
        else: m -= 1
    print(''.join(reversed(ans)))
if __name__ == '__main__':
    sys.exit(main())