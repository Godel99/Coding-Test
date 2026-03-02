import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque

def main():
    n = int(input())
    board = [list(map(int, input().strip())) for _ in range(n)]
    ans = []
    for i in range(n):
        for j in range(n):
            if not board[i][j]: continue
            board[i][j] = 0
            cnt = 1
            dq = deque([(i, j)])
            while dq:
                x, y = dq.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x+dx, y+dy
                    if not (0 <= nx < n) or not (0 <= ny < n): continue 
                    if board[nx][ny]:
                        board[nx][ny] = 0
                        cnt += 1
                        dq.append((nx, ny))
            ans.append(cnt)
    ans.sort()
    print(len(ans))
    if ans: print('\n'.join(map(str, ans)))
if __name__ == '__main__':
    main()