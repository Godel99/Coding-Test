import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())+1; n = int(input())
        dp = [i for i in range(n+1)]
        for _ in range(1, k):
            for i in range(2, n+1):
                dp[i] += dp[i-1]
        print(dp[n])
    return 0
if __name__ == '__main__':
    sys.exit(main())