import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    k = int(input())
    maxl = a[-1]
    dp = [[0] * (maxl+1) for _ in range(k)]
    dp[0][0] = 1
    ans = 0
    from math import comb
    for i in range(n):
        if i >= k-1:
            total = comb(i, k-1)
            ncnt = sum(dp[k-1][:a[i]+1])
            ans += total-ncnt
        for j in range(min(k-1, i+1), 0, -1):
            for l in range(maxl, a[i]-1, -1):
                dp[j][l] += dp[j-1][l-a[i]]
    print(ans)    
if __name__ == "__main__":
    main()