import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque
from math import inf
import heapq

def main():
    n, m = map(int, input().split())
    e = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        e[x].append(y)
        e[y].append(x)
    ans = []
    for i in range(1, n+1):
        dp = [inf]*(n+1)
        dq = deque([i])
        dp[i] = 0
        while dq:
            cur = dq.popleft()
            for nxt in e[cur]:
                if dp[nxt] > dp[cur]+1:
                    dp[nxt] = dp[cur]+1
                    dq.append(nxt)
        heapq.heappush(ans, (sum(dp[i] for i in range(1, n+1) if dp[i] != inf), i))
    print(heapq.heappop(ans)[1])
    return 0
if __name__ == '__main__':
    sys.exit(main())