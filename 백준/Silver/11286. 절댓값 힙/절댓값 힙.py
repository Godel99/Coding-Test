import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

import heapq

def main():
    n = int(input())
    pos_hq = []
    neg_hq = []
    for i in range(n):
        x = int(input())
        if x > 0: heapq.heappush(pos_hq, x)
        elif x < 0: heapq.heappush(neg_hq, -x)
        else:
            if pos_hq and not neg_hq: print(heapq.heappop(pos_hq)); continue
            if not pos_hq and neg_hq: print(-heapq.heappop(neg_hq)); continue
            if not pos_hq and not neg_hq: print(0); continue
            if pos_hq[0] >= neg_hq[0]: print(-heapq.heappop(neg_hq))
            else: print(heapq.heappop(pos_hq))
if __name__ == '__main__':
    main()