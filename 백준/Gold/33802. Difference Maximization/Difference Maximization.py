import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    A = [0]*(n+1); dmin = dmax = ans = 0
    for a in list(map(int, input().split())):
        if a:
            dmin += a-1
            dmax += m-a
        A[a] += 1
    s = 0
    for i in range(1, m+1):
        s += A[i]
        ans += s*(n-A[0]-s)
    while A[0]:
        if dmin < dmax:
            dmin += m-1
            ans += dmax
        else:
            dmax += m-1
            ans += dmin
        A[0] -= 1
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())