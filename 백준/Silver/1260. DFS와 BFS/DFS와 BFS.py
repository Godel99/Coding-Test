import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque

def main():
    n, m, v = map(int, input().split())
    edge = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        edge[x].append(y)
        edge[y].append(x)
    for e in edge: e.sort()
    visited = [False]*(n+1)
    def dfs(v):
        visited[v] = True
        print(v, end=' ')
        for nxt in edge[v]:
            if not visited[nxt]: dfs(nxt)
    dfs(v)
    print()
    visited = [False]*(n+1)
    def bfs(v):
        visited[v] = True
        dq = deque([v])
        while dq:
            cur = dq.popleft()
            print(cur, end=' ')
            for nxt in edge[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dq.append(nxt)
    bfs(v)
if __name__ == '__main__':
    sys.exit(main())