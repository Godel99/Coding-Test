import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
sys.setrecursionlimit(2000)

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    ans = 0
    maxv = max(map(max, board))
    def dfs(x, y, d, s):
        nonlocal ans
        if s+maxv*(4-d) <= ans: return
        if d == 4: ans = max(ans, s); return
        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            if 0 > nx or nx >= n or 0 > ny or ny >= m or visited[nx][ny]: continue
            if d == 2:
                visited[nx][ny] = 1
                dfs(x, y, d+1, s+board[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, d+1, s+board[nx][ny])
            visited[nx][ny] = 0
    for i in range(n):
        for j in range(m):
            visited[i][j] = 1
            dfs(i, j, 1, board[i][j])
            visited[i][j] = 0
    print(ans)
if __name__ == '__main__':
    main()