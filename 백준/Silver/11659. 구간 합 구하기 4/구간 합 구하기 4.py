import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from itertools import accumulate

def main():
    n, m = map(int, input().split())
    a = tuple(map(int , input().split()))
    pre_sum = tuple(accumulate(a, initial=0))
    for _ in range(m):
        i, j = map(int, input().split())
        print(pre_sum[j]-pre_sum[i-1])
    return 0
if __name__ == '__main__':
    sys.exit(main())