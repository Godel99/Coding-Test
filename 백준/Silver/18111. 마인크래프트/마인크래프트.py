import sys # 18111
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from math import inf

def main():
    n, m, b = map(int, input().split())
    min_h , max_h = 256, 0
    height = [0]*257
    for _ in range(n):
        field = list(map(int, input().split()))
        for h in field:
            if min_h > h: min_h = h
            if max_h < h: max_h = h
            height[h] += 1
    min_t, best_h = inf, 0
    for tar in range(min_h, max_h+1):
        up = down = 0
        for h in range(min_h, max_h+1):
            if h > tar: down += (h-tar)*height[h]
            else: up += (tar-h)*height[h]
        if down+b >= up: 
            cur_t = down*2+up
            if cur_t <= min_t:
                min_t = cur_t
                besth = tar
    print(min_t, besth)
if __name__ == '__main__':
    main()