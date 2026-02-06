import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()
#MOD = 1_000_000_007

def main():
    n, m = map(int , input().split())
    def cp(n, m):
        cnt = 0
        while n >= m:
            n //= m
            cnt += n
        return cnt
    cnt2 = cp(n, 2)-cp(m, 2)-cp(n-m, 2)
    cnt5 = cp(n, 5)-cp(m, 5)-cp(n-m, 5)
    print(min(cnt2, cnt5))
    return 0
if __name__ == '__main__':
    sys.exit(main())