import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

from collections import deque

def main():
    n, k = map(int, input().split())
    q = deque(list(range(1, n+1)))
    ans = []
    while q:
        q.rotate(-(k-1))
        ans.append(str(q.popleft()))
    print(f'<{", ".join(ans)}>')
if __name__ == '__main__':
    main()