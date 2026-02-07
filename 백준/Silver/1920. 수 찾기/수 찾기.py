import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    for b in B:
        if b in A: print(1)
        else: print(0)
    return 0
if __name__ == '__main__':
    sys.exit(main())