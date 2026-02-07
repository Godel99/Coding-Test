import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from math import gcd

def main():
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        A = tuple(map(int, input().split()))
        g = 0
        for a in A[1:]: g = gcd(a, g)
        if x % g or y % g: print('Gave up')
        else: print('Ta-da')
    return 0
if __name__ == '__main__':
    sys.exit(main())