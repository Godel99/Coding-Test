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
        pre = -1
        for i in range(n):
            if not visited[i] and a[i] != pre:
                visited[i] = 1
                ans.append(a[i])
                pre = a[i]
                dfs(i+1, d+1)
                ans.pop()
                visited[i] = 0
    dfs(0, 0)
if __name__ == '__main__':
    main()