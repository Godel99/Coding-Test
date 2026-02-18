import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import deque

def main():
    n = int(input()); m = int(input())
    e = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        e[x].append(y)
        e[y].append(x)
    visited = [False]*(n+1); visited[1] = True
    dq = deque([1])
    ans = 0
    while dq:
        cur = dq.popleft()
        for nxt in e[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                ans += 1
                dq.append(nxt)
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())