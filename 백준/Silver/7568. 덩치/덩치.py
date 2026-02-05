import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()
#MOD = 1_000_000_007

def main():
    n = int(input())
    p = [tuple(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        r = 1
        for j in range(n):
            if p[i][0] < p[j][0] and p[i][1] < p[j][1]: r += 1
        print(r, end=' ')
    return 0
if __name__ == '__main__':
    sys.exit(main())