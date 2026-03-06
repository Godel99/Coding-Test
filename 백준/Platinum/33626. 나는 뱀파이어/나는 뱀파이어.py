import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

sys.setrecursionlimit(200000)

def main():
    n, m, p = map(int, input().split())
    e = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        e[u].append(v)
        e[v].append(u)
    def dfs(cur, pre, t):
        nonlocal cnt
        ret = t+1
        for nxt in e[cur]:
            if nxt == pre: continue
            ret = min(ret, dfs(nxt, cur, t)+1)
        if ret > t and cur != p:
            ret = 0
            cnt += 1
        return ret
    l, r = 0, n
    while l < r:
        mid = l+r>>1
        cnt = 0
        dfs(p, 0, mid)
        if cnt <= m: r = mid
        else: l = mid+1
    if l == n: print(-1)
    else: print(l+1)
if __name__ == '__main__':
    main()