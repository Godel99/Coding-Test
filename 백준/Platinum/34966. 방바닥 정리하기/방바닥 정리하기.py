import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque
from math import inf

dx = (1, -1, 0, 0); dy = (0, 0, 1, -1)

def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    start = end = None
    isa = isb = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'A': start = (i, j)
            if a[i][j] == 'B': end = (i, j)
            if a[i][j] == 'a': isa = 1
            if a[i][j] == 'b': isb = 1
    if not isa and not isb: print(0); return 0
    if not isa or not isb: print(1); return 0
    def solved(start, end, type):
        ay, ax = start; by, bx = end
        dq = [deque() for _ in range(3)]
        dp = [[inf]*n for _ in range(n)]
        dq[0].append(start)
        dp[ay][ax] = 0
        res = 0
        while any(dq):
            while not dq[res%3]: res += 1
            while dq[res%3]:
                y, x = dq[res%3].popleft()
                if dp[y][x] < res: continue
                for dir in range(4):
                    ny = y+dy[dir]; nx = x+dx[dir]
                    if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
                    nd = dp[y][x]+(a[ny][nx] == ['a', 'b'][type^(res&1)]) 
                    if a[ny][nx] == ['b', 'a'][type] and not res: nd = 2
                    if dp[ny][nx] <= nd: continue
                    dp[ny][nx] = nd; dq[nd%3].append((ny, nx))
        if dp[by][bx] > 1: return inf
        return res
    ans = inf; ans = min(ans, solved(start, end, 0), solved(end, start, 1))
    if ans == inf: print(-1)
    else: print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())