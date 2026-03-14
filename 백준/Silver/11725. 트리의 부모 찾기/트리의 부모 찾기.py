import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque

def main():
    n = int(input())
    e = [[] for _ in range(n+1)]
    par = [-1]*(n+1)
    for _ in range(n-1):
        x, y = map(int, input().split())
        e[x].append(y)
        e[y].append(x)
    dq = deque([1])
    par[1] = 1
    while dq:
        cur = dq.popleft()
        for nxt in e[cur]:
            if par[nxt] == -1:
                par[nxt] = cur
                dq.append(nxt)
    for p in par[2:]: print(p)
if __name__ == '__main__':
    main()