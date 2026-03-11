import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    visited = [0]*n
    ans = []
    def dfs(x, d):
        if d == m:
            print(*ans)
            return
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                ans.append(a[i])
                dfs(i, d+1)
                ans.pop()
                visited[i] = 0
    dfs(0, 0)
if __name__ == '__main__':
    main()