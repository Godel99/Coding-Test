import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

import heapq

def main():
    n = int(input())
    hq = []
    for _ in range(n):
        x = int(input())
        if x: heapq.heappush(hq, x)
        else: print(heapq.heappop(hq) if hq else 0)
    return 0
if __name__ == '__main__':
    sys.exit(main())