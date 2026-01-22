import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, m, k = map(int, input().split())
    if n == m: return print(-1)
    ans = []
    ans.extend(range(1, k))
    ans.append(n)
    ans.extend(range(k, m))
    ans.extend(range(n-1, m-1, -1))
    print(*ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())