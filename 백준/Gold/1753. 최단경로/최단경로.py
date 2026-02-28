import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque
from math import inf

def main():
    n, e = map(int, input().split())
    k = int(input())
    g = [[] for _ in range(n+1)]
    dq = [deque() for _ in range(11)]
    dp = [inf]*(n+1)
    for _ in range(e):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
    dp[k] = 0
    dq[1].append(k)
    h = 1
    while any(dq):
        while not dq[h%11]: h +=1
        while dq[h%11]:
            cur = dq[h%11].popleft()
            for nxt, w in g[cur]:
                if dp[nxt] > dp[cur]+w:
                    dp[nxt] = dp[cur]+w
                    dq[(dp[cur]+w)%11].append(nxt)
    ans = []
    for i in range(1, n+1):
        ans.append(str(dp[i]) if dp[i] != inf else 'INF')
    print('\n'.join(ans))
    return 0
if __name__ == '__main__':
    sys.exit(main())