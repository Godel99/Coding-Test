import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

import heapq
from collections import deque

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dq = deque([v, i] for i, v in enumerate(map(int, input().split())))
        hq = []
        for v, _ in dq: heapq.heappush(hq, -v)
        cnt = 0
        while dq:
            v, i = dq.popleft()
            if v == -hq[0]:
                cnt += 1
                heapq.heappop(hq)
                if i == m:
                    print(cnt)
                    break
            else: dq.append((v, i))
    return 0
if __name__ == '__main__':
    sys.exit(main())