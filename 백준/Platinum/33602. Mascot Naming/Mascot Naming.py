import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n = int(input())
    ss = [input() for _ in range(n)]
    t = input()
    ch = [[] for _ in range(len(t))]
    for s in ss:
        r = 0
        for c in s:
            if c == t[r]:
                r += 1
                if r == len(t): print('NO'); return 0
            else: ch[r].append(c)
    print('YES')
    for i, tc in enumerate(t):
        for c in ch[i]: print(c, end='')
        if i < len(t)-1: print(tc, end='')
    return 0
if __name__ == '__main__':
    sys.exit(main())