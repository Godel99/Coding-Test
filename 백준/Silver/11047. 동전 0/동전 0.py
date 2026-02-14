import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    ans = 0
    for x in a[::-1]:
        if k == 0: break
        ans += k//x
        k %= x
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())