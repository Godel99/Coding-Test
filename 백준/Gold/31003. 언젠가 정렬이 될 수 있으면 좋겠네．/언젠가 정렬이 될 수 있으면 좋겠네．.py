import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

import heapq
from math import gcd

def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    e = [[] for _ in range(n)]
    deg = [0]*n
    for i in range(n):
        for j in range(i):
            if gcd(a[j], a[i]) != 1: 
                e[j].append(i)
                deg[i] += 1
    hq = []
    for i in range(n):
        if deg[i] == 0: heapq.heappush(hq, (a[i], i))
    while hq:
        cur = heapq.heappop(hq)[1]
        print(a[cur], end=' ')
        for nxt in e[cur]:
            deg[nxt] -= 1
            if deg[nxt] == 0: heapq.heappush(hq, (a[nxt], nxt))
    return 0
if __name__ == '__main__':
    sys.exit(main())