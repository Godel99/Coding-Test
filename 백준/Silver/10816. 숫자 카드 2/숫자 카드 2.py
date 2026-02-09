import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import defaultdict

def main():
    n = int(input())
    d = defaultdict(int)
    for a in input().split():
        d[a] += 1
    m = int(input())
    ans = []
    for a in input().split():
        if a in d: ans.append(d[a])
        else: ans.append(0)
    print(' '.join(map(str, ans)))
    return 0
if __name__ == '__main__':
    sys.exit(main())