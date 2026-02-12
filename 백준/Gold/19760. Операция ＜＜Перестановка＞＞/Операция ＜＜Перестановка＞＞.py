import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import deque

def main():
    n, m = map(int, input().split())
    deg = [0]*(n+1)
    e = [[] for _ in range(n+1)]
    for i in range(1, m+1):
        x, y = map(int, input().split())
        e[x].append((y, i))
        deg[y] += 1
    dq = deque()
    for i in range(1, n+1):
        if not deg[i]: dq.append(i)
    ans = 0
    while dq:
        if len(dq) > 1: return int(not print(-1))
        cur = dq.popleft()
        for nxt, idx in e[cur]:
            deg[nxt] -= 1
            if not deg[nxt]: 
                dq.append(nxt)
                ans = max(ans, idx)
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())