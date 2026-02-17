import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    dp = [0]*(n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1]+1
        if i%2 == 0: dp[i] = min(dp[i], dp[i//2]+1)
        if i%3 == 0: dp[i] = min(dp[i], dp[i//3]+1)
    print(dp[n])
    return 0
if __name__ == '__main__':
    sys.exit(main())