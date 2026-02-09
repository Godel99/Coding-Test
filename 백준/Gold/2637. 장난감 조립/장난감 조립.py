import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import deque

def main():
    n = int(input()); m = int(input())
    indeg = [0]*(n+1)
    need = [[0]*(n+1) for _ in range(n+1)]
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y, k = map(int, input().split())
        g[y].append((x, k))
        indeg[x] += 1
    q = deque([])
    for i in range(1, n+1):
        if not indeg[i]:
            q.append(i)
            need[i][i] = 1
    while q:
        now = q.popleft()
        for nxt, k in g[now]:
            for i in range(1, n+1):
                need[nxt][i] += need[now][i]*k
            indeg[nxt] -= 1
            if not indeg[nxt]: q.append(nxt)
    for i in range(1, n+1):
        if need[n][i]: print(i, need[n][i])
    return 0
if __name__ == '__main__':
    sys.exit(main())