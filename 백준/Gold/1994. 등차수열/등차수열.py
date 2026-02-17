import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]; 
    a.sort()
    dp = [{} for _ in range(n)]
    ans = 1
    for i in range(n):
        for j in range(i):
            d = a[i]-a[j]
            if d in dp[j]: dp[i][d] = dp[j][d]+1
            else: dp[i][d] = 2
            ans = max(ans, dp[i][d])
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())