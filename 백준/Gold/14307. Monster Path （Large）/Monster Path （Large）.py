import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    T = int(input())
    def sv():
        r, c, sy, sx, s = map(int, input().split()); sy += 1; sx += 1
        p, q = map(float, input().split())
        board = [['']*(c+1) for _ in range(r+1)]
        d = [[0.0]*(c+1) for _ in range(r+1)]
        dy = (-1, 0, 1, 0); dx = (0, 1, 0, -1)
        for i in range(1, r+1):
            row = input().split()
            for j in range(1, c+1):
                board[i][j] = row[j-1]
                if board[i][j] == 'A': d[i][j] = p
                else: d[i][j] = q
        ans = 0
        for l in range(1<<(2*s)):
            y = sy; x = sx; sump = 0; flag = 1
            for i in range(s):
                k = (l>>(i*2))&3
                y += dy[k]; x += dx[k]
                if y < 1 or  y > r or x < 1 or x > c: flag = 0; continue
                sump += d[y][x]
                if board[y][x] == 'A': d[y][x] *= 1-p
                else: d[y][x] *= 1-q
            if flag: ans = max(ans, sump)
            y = sy; x = sx
            for i in range(s):
                k = (l>>(i*2))&3
                y += dy[k]; x += dx[k]
                if y < 1 or  y > r or x < 1 or x > c: continue
                if board[y][x] == 'A': d[y][x] = p
                else: d[y][x] = q
        return ans
    for i in range(1, T+1): print(f'Case #{i}: {sv():.7f}')
    return 0
if __name__ == '__main__':
    sys.exit(main())