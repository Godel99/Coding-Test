import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

def main():
    m, n = map(int, input().split())
    tomato = [list(map(int, input().split())) for _ in range(n)]
    dq = deque()
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1: dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            if not (0 <= nx < n) or not (0 <= ny < m): continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y]+1
                dq.append((nx, ny))
    ans = 0
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                print(-1)
                return
            ans = max(ans, tomato[i][j])
    print(ans-1)
if __name__ == '__main__':
    main()