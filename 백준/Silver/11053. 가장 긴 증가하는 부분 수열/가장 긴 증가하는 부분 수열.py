import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1]*n
    ans = 1
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]: dp[i] = max(dp[i], dp[j]+1)
            if ans < dp[i]: ans = dp[i]
    print(ans)
if __name__ == '__main__':
    main()