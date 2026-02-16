import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    score = [0]+[int(input()) for _ in range(n)]
    if n == 1: return int(not print(score[1]))
    if n == 2: return int(not print(score[1]+score[2]))
    dp = [0]*(n+1)
    dp[1] = score[1]
    dp[2] = score[1]+score[2]
    dp[3] = max(score[1], score[2])+score[3]
    for i in range(4, n+1): dp[i] = max(dp[i-3]+score[i-1], dp[i-2])+score[i]
    print(dp[n])
    return 0
if __name__ == '__main__':
    sys.exit(main())