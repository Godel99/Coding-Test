import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from math import inf
from collections import deque

def main():
    n, m = map(int, input().split())
    board = [inf]*101
    e = {}
    for _ in range(n+m):
        x, y = map(int, input().split())
        e[x] = y
    board[1] = 0
    dq = deque([1])
    while dq:
        cur = dq.popleft()
        for i in range(1, 7):
            nxt = cur+i
            if nxt <= 100 and board[nxt] == inf:
                board[nxt] = min(board[nxt], board[cur]+1)
                if nxt in e: 
                    nxt = e[nxt]
                    board[nxt] = min(board[nxt], board[cur]+1)
                dq.append(nxt)
    print(board[-1])
if __name__ == '__main__':
    main()