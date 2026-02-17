import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import defaultdict
from math import prod

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        data = defaultdict(int)
        for _ in range(n):
            _, s = input().split()
            data[s] += 1
        print(prod(c+1 for c in data.values())-1)
    return 0
if __name__ == '__main__':
    sys.exit(main())