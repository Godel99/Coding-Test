import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def dist(x, y):
    x = abs(x); y = abs(y)
    return x*x + y*y

def main():
    sx, sy = map(int, input().split())
    if not sx and not sy: return not print(-1)
    s = input()
    dx = (1, 0, -1, 0); dy = (0, 1, 0, -1)
    x = -sx; y = -sy
    ax = x; ay = y
    idx = 0; dir = 0
    while idx < len(s):
        op = s[idx]; idx += 1
        d = 0
        while idx < len(s) and s[idx].isdigit(): d = d*10+int(s[idx]); idx += 1
        if op == 'S':
            nx = x+d*dx[dir]; ny = y+d*dy[dir]
            if x*nx <= 0 and y*ny <= 0: return not print(-1)
            if dist(nx, ny) < dist(ax, ay): ax = nx; ay = ny
            if x*nx < 0: 
                if dist(0, y) < dist(ax, ay): ax = 0; ay = y
            if y*ny < 0:
                if dist(x, 0) < dist(ax, ay): ax = x; ay = 0
            x = nx; y = ny
        if op == 'T':
            dir += d; dir %= 4
    print(ax+sx, ay+sy)
    return 0
if __name__ == '__main__':
    sys.exit(main())