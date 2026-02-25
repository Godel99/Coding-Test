import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

dx = (1, -1, 0, 0); dy = (0, 0, 1, -1)

def main():
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'I': 
                sx, sy = (i, j)
                break
    visited[sx][sy] = True
    st = [(sx, sy)]
    ans = 0
    while st:
        x, y = st.pop()
        if board[x][y] == 'P': ans += 1
        for dir in range(4):
            nx = x+dx[dir]; ny = y+dy[dir]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] != 'X':
                visited[nx][ny] = True
                st.append((nx, ny))
    if ans: print(ans)
    else: print('TT')
    return 0
if __name__ == '__main__':
    sys.exit(main())