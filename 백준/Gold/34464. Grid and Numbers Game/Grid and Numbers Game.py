import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

dx = (1, -1, 0, 0); dy = (0, 0, 1, -1)

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        d = [[-1]*(m+2) for _ in range(n+2)]
        v = []
        for i in range(1, n+1):
            a = tuple(map(int, input().split()))
            for j in range(1, m+1):
                v.append((a[j-1], i, j))
        v.sort()
        for _, i, j in v:
            for dir in range(4): d[i][j] = max(d[i][j], d[i+dy[dir]][j+dx[dir]]+1)
        ans = 0
        for x, i, j in v: ans ^= (x-d[i][j])
        print('Yes' if ans&1 else 'No')
    return 0
if __name__ == '__main__':
    sys.exit(main())