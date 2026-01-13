import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = [0, 0, 0, 0]+list(map(int, input().split()))
    a.sort()
    dp = [0]*(n+4)
    for i in range(4, n+4):
        dp[i] = dp[i-1]+1
        if a[i]-a[i-1] <= 20: dp[i] = min(dp[i], dp[i-2]+1)
        if a[i]-a[i-2] <= 10: dp[i] = min(dp[i], dp[i-3]+1)
    print(dp[n+3])
if __name__ == '__main__':
    main()