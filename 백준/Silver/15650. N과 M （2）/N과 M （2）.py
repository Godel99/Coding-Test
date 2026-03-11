import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n, m = map(int, input().split())
    ans = []
    def dfs(x, d):
        if d == m:
            print(*ans)
            return
        for i in range(x, n+1):
            ans.append(i)
            dfs(i+1, d+1)
            ans.pop()
    dfs(1, 0)
if __name__ == '__main__':
    main()