import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()
#MOD = 1_000_000_007

from collections import deque
dx = (1, 0, -1, 0); dy = (0, 1, 0, -1)

def main():
    n, m = map(int, input().split())
    board = [[i for i in input()] for _ in range(n)]
    dp = [[[0]*2 for _ in range(m)] for _ in range(n)]
    dp[0][0][0] = 1
    dq = deque([(0, 0, 0)])
    while dq:
        x, y, b = dq.popleft()
        if x == n-1 and y == m-1: return int(not print(dp[x][y][b]))
        for dir in range(4):
            nx = x+dx[dir]; ny = y+dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if board[nx][ny] == '0' and dp[nx][ny][b] == 0:
                dp[nx][ny][b] = dp[x][y][b]+1 
                dq.append((nx, ny, b))
            if board[nx][ny] == '1' and b == 0 and dp[nx][ny][1] == 0:
                dp[nx][ny][1] = dp[x][y][b]+1
                dq.append((nx, ny, 1))
    print(-1)
    return 0
if __name__ == '__main__':
    sys.exit(main())