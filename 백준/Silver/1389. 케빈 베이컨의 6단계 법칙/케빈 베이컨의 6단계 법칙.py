import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque
from math import inf

def main():
    n, m = map(int, input().split())
    e = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        e[x].append(y)
        e[y].append(x)
    min_d = inf
    ans = 0
    for i in range(1, n+1):
        dist = [-1]*(n+1)
        dq = deque([i])
        dist[i] = 0
        while dq:
            cur = dq.popleft()
            for nxt in e[cur]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[cur]+1
                    dq.append(nxt)
        sum_d = sum(dist)+1
        if min_d > sum_d:
            min_d = sum_d
            ans = i
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())