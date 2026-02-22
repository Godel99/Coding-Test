import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

dx = (1, -1, 0, 0); dy = (0, 0, 1, -1)

def main():
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        board = [[0]*(m) for _ in range(n)]
        visited = [[False]*(m) for _ in range(n)]
        cnt = 0
        for _ in range(k):
            x, y = map(int, input().split())
            board[y][x] = 1
        for i in range(n):
            for j in range(m):
                if board[i][j] and not visited[i][j]:
                    cnt += 1
                    visited[i][j] = True
                    st = [(i, j)]
                    while st:
                        x, y = st.pop()
                        for dir in range(4):
                            nx, ny = x+dx[dir], y+dy[dir]
                            if 0 <= nx < n and 0 <= ny < m:
                                if board[nx][ny] and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    st.append((nx, ny))
        print(cnt)
    return 0
if __name__ == '__main__':
    sys.exit(main())