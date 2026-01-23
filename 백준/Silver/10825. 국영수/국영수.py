import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    ar = [list(input().split()) for _ in range(n)]
    ar.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    for a in ar: print(a[0])
    return 0
if __name__ == '__main__':
    sys.exit(main())