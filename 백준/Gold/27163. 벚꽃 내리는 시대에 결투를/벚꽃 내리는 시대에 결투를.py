import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, a, l = map(int, input().split())
    dp = [[-1]*(l+1) for _ in range(n+1)]
    way = [[False]*(l+1) for _ in range(n+1)]
    ld = [0]*(n+1)
    for i in range(1, l+1): dp[0][i] = a
    for i in range(1, n+1):
        adam, ldam = map(int, input().split())
        ld[i] = ldam
        if adam == -1:
            for j in range(l, ldam, -1):
                if dp[i-1][j] != -1:
                    dp[i][j-ldam] = dp[i-1][j]
                    way[i][j-ldam] = True
        elif ldam == -1:
            for j in range(l, 0, -1):
                if dp[i-1][j] != -1:
                    dp[i][j] = max(0, dp[i-1][j]-adam)
                    way[i][j] = False
        else:
            for j in range(1, l+1):
                if dp[i-1][j] >= adam:
                    dp[i][j] = dp[i-1][j]-adam
                    way[i][j] = False
                if j > ldam and dp[i][j-ldam] < dp[i-1][j]:
                    dp[i][j-ldam] = dp[i-1][j]
                    way[i][j-ldam] = True
    if dp[n][1] != -1:
        print('YES')
        life = 1
        st = []
        for i in range(n, 0, -1):
            if way[i][life]:
                st.append('L')
                life += ld[i]
            else: st.append('A')
        print(''.join(reversed(st)))
    else: print('NO')
    return 0
if __name__ == '__main__':
    sys.exit(main())