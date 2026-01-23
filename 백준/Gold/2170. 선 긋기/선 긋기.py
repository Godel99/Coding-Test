import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    lines = sorted([tuple(map(int, input().split())) for _ in range(n)])
    total = 0
    start, end = lines[0]
    for s, e in lines[1:]:
        if s > end:
            total += end-start
            start, end = s, e
        else:
            end = max(end, e)
    total += end-start
    print(total)
    return 0
if __name__ == '__main__':
    sys.exit(main())