import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import defaultdict

def main():
    n = int(input())
    d = defaultdict(int)
    for a in map(int, input().split()):
        d[a] += 1
    m = int(input())
    for a in map(int, input().split()):
        if a in d: print(d[a], end=' ')
        else: print(0, end=' ')
    return 0
if __name__ == '__main__':
    sys.exit(main())