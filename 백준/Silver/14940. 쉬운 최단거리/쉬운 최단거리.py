import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    start = None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2: 
                board[i][j] = 0
                visited[i][j] = 1
                start = (i, j)
                break
        if start: break
    dq = deque([start])
    while dq:
        x, y = dq.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n) or not (0 <= ny < m): continue
            if board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                board[nx][ny] = board[x][y]+1
                dq.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j]: print(-1, end=' ')
            else: print(board[i][j], end=' ')
        print()
    return 0
if __name__ == '__main__':
    main()