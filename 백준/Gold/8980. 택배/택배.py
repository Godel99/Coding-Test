import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, c = map(int, input().split())
    m = int(input())
    d = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x: x[1])
    cap = [0] * (n+1)
    ans = 0
    for s, e, w in d:
        maxu = max(cap[s:e])
        can = min(w, c-maxu)
        for i in range(s, e): cap[i] += can
        ans += can
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())