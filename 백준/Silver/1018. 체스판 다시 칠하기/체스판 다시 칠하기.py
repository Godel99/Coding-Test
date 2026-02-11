import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    min_d = 64
    for i in range(n-7):
        for j in range(m-7):
            d = 0
            for r in range(i, i+8):
                for c in range(j, j+8):
                    if (r+c)%2:
                        if board[r][c] != 'W': d += 1
                    else:
                        if board[r][c] != 'B': d += 1
            min_d = min(min_d, d, 64-d)
    print(min_d)
    return 0
if __name__ == '__main__':
    sys.exit(main())