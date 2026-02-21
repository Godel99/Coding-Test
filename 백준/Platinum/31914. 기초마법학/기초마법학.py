import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

import heapq

def main():
    n, k = map(int, input().split())
    cnt = [0]*(k+1)
    g = [tuple(map(int, input().split())) for _ in range(n)]
    g.sort()
    ans = cur = 0
    maxh = 123456789
    max_hq = []
    for i in range(n):
        x, y, p, c = g[i]
        heapq.heappush(max_hq, (-y, p, c))
        cur += p
        if not cnt[c]: cnt[0] += 1
        cnt[c] += 1
        if i == n-1 or g[i+1][0] != x:
            while max_hq:
                yy = -max_hq[0][0]
                if cnt[0] != k and yy <= maxh: break
                _, pp, cc = heapq.heappop(max_hq)
                cur -= pp
                cnt[cc] -= 1
                if not cnt[cc]: cnt[0] -= 1
                maxh = min(maxh, yy-1)
            ans = max(ans, cur)    
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())