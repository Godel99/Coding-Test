import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

dx = (1, -1, 0, 0); dy = (0, 0, 1, -1)

def main():
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'I': 
                sx, sy = (i, j)
                break
    st = [(sx, sy)]
    ans = 0
    while st:
        x, y = st.pop()
        for dir in range(4):
            nx = x+dx[dir]; ny = y+dy[dir]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'X':
                if board[nx][ny] == 'P': ans += 1
                board[nx][ny] = 'X'
                st.append((nx, ny))
    if ans: print(ans)
    else: print('TT')
    return 0
if __name__ == '__main__':
    sys.exit(main())