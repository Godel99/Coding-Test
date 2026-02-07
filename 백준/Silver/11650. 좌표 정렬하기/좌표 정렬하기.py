import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    A = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))
    for a in A: print(a[0], a[1])
    return 0
if __name__ == '__main__':
    sys.exit(main())