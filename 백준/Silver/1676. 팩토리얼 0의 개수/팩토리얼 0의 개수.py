import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()
#MOD = 1_000_000_007

def main():
    n = int(input())
    cnt = 0; f = 5
    while f <= n:
        cnt += n // f
        f *= 5
    print(cnt)
    return 0
if __name__ == '__main__':
    sys.exit(main())