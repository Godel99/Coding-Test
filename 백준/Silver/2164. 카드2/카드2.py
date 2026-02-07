import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import deque

def main():
    n = int(input())
    a = deque([i for i in range(1, n+1)])
    while a:
        ans = a.popleft()
        a.rotate(-1)
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())