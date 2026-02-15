import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = [[0, 0] for _ in range(n+2)]
        dp[0] = [1, 0]; dp[1] = [0, 1]
        for i in range(2, n+2): 
            dp[i][0] = dp[i-1][0]+dp[i-2][0]
            dp[i][1] = dp[i-1][1]+dp[i-2][1]
        print(*dp[n])
    return 0
if __name__ == '__main__':
    sys.exit(main())