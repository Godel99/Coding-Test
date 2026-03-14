import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque

def main():
    n = int(input())
    e = [[] for _ in range(n+1)]
    par = [0]*(n+1)
    for _ in range(n-1):
        x, y = map(int, input().split())
        e[x].append(y)
        e[y].append(x)
    dq = deque([1])
    par[1] = 1
    while dq:
        cur = dq.popleft()
        for nxt in e[cur]:
            if not par[nxt]:
                par[nxt] = cur
                dq.append(nxt)
    print('\n'.join(map(str, par[2:])))
if __name__ == '__main__':
    main()