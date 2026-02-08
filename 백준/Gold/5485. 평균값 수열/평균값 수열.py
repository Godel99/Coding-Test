import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    low = int(input())
    high = cur = int(input())
    for _ in range(2, n):
        nxt = int(input())
        low, high = 2*cur-high, min(2*cur-low, nxt)
        cur = nxt
    print(max(0, high-low+1))
    return 0
if __name__ == '__main__':
    sys.exit(main())