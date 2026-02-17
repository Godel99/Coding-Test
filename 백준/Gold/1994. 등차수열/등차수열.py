import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input()); 
    if n == 1: return int(not print(1))
    a = [int(input()) for _ in range(n)]; 
    a.sort()
    b = [0]*n
    m = cnt = 0
    ans = 2
    for i in range(n):
        if i == 0 or a[i] != a[i-1]:
            b[m] = a[i]
            m += 1
            cnt = 1
        else: cnt += 1
        ans = max(ans, cnt)
    dp = [[0]*m for _ in range(m)]
    for i in range(1, m):
        l = i-1; r = i+1
        while l >= 0 and r < m:
            if b[l]+b[r] == 2*b[i]:
                dp[i][r] = dp[l][i]+1
                ans = max(ans, dp[i][r]+2)
                l -= 1; r += 1
            elif b[l]+b[r] < 2*b[i]:
                ans = max(ans, dp[i][r])
                r += 1
            else: l -= 1
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())