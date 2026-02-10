import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    x = list(map(int, input().split()))
    now = x[0]
    dp = [1]*now
    for i in range(1, n):
        while now > x[i]:
            dp[now-1-x[i]] += dp[now-1]
            now -= 1
    ans = 0
    for i in range(1, now): ans += i*dp[i]
    print(f'{ans/x[0]:.12f}')
    return 0
if __name__ == '__main__':
    sys.exit(main())