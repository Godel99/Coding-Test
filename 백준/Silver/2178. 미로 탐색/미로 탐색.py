import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

dx = (1, -1, 0, 0); dy = (0, 0, 1, -1)
from collections import deque

def main():
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    dq = deque([(0, 0)])
    while dq:
        x, y = dq.popleft()
        for dir in range(4):
            nx = x+dx[dir]; ny = y+dy[dir]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if board[nx][ny] == '1' and not dp[nx][ny]:
                dp[nx][ny] = dp[x][y]+1
                dq.append((nx, ny))
    print(dp[n-1][m-1])
    return 0
if __name__ == '__main__':
    sys.exit(main())