import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n, m = map(int, input().split())
    a = sorted(set(map(int, input().split())))
    ans = []
    def dfs(x):
        if len(ans) == m:
            print(*ans)
            return
        for i in range(x, len(a)):
            ans.append(a[i])
            dfs(i)
            ans.pop()
    dfs(0)
if __name__ == '__main__':
    main()