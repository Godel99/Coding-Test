import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

import heapq

def main():
    n, k = map(int, input().split())
    gems = sorted([tuple(map(int, input().split())) for _ in range(n)])
    bags = sorted(int(input()) for _ in range(k))
    hq = []
    idx = ans = 0
    for bag in bags:
        while idx < n  and gems[idx][0] <= bag:
            heapq.heappush(hq, -gems[idx][1])
            idx += 1
        if hq: ans += -heapq.heappop(hq)
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())