import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n < 4: 
            print(1); 
            continue
        dp = [0]*(n+1)
        dp[1] = dp[2] = dp[3] = 1
        for i in range(4, n+1):
            dp[i] = dp[i-3]+dp[i-2]
        print(dp[n])
    return 0
if __name__ == '__main__':
    sys.exit(main())