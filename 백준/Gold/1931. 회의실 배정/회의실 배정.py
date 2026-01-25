import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    I = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
    ans = 1
    end = I[0][1]
    for s, e in I[1:]:
        if s >= end:
            ans += 1
            end = e
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())