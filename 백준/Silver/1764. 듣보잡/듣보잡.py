import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    s = set()
    cnt = 0
    ans = []
    for _ in range(n): s.add(input())
    for _ in range(m):
        name = input()
        if name in s:
            cnt += 1
            ans.append(name)
    ans.sort()
    print(cnt)
    print('\n'.join(ans))
    return 0
if __name__ == '__main__':
    sys.exit(main())