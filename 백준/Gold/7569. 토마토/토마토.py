import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque

dz, dy, dx = (1, -1, 0, 0, 0, 0), (0, 0, 0, 0, 1, -1), (0, 0, 1, -1, 0, 0)

def main():
    m, n, h = map(int, input().split())
    tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    dq = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == 1: dq.append((i, j, k))
    while dq:
        z, y, x = dq.popleft()
        for dir in range(6):
            nz, ny, nx = z+dz[dir], y+dy[dir], x+dx[dir]
            if not (0 <= nz < h) or not (0 <= ny < n) or not (0 <= nx < m): continue
            if tomato[nz][ny][nx] == 0:
                 tomato[nz][ny][nx] = tomato[z][y][x]+1
                 dq.append((nz, ny, nx))
    ans = 0
    for flo in tomato:
        for r in flo:
            for c in r:
                if c == 0:
                    print(-1)
                    return
                ans = max(ans, c)
    print(ans-1 if ans else 0)
if __name__ == '__main__':
    main()