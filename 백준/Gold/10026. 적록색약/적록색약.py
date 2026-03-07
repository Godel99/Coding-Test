import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

def main():
    n = int(input())
    board = [list(input()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    cnt1 = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                c = board[i][j]
                dq = deque([(i,j)])
                visited[i][j] = 1
                while dq:
                    x, y = dq.popleft()
                    for dir in range(4):
                        nx, ny = x+dx[dir], y+dy[dir]
                        if not (0 <= nx < n) or not (0 <= ny < n): continue
                        if board[nx][ny] == c and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            dq.append((nx, ny))
                cnt1 += 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'G': board[i][j] = 'R'
    cnt2 = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                c = board[i][j]
                dq = deque([(i,j)])
                visited[i][j] = 1
                while dq:
                    x, y = dq.popleft()
                    for dir in range(4):
                        nx, ny = x+dx[dir], y+dy[dir]
                        if not (0 <= nx < n) or not (0 <= ny < n): continue
                        if board[nx][ny] == c and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            dq.append((nx, ny))
                cnt2 += 1
    print(cnt1, cnt2)
if __name__ == '__main__':
    main()