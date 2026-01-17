import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    ans = [-1] * (n+1)
    while m:
        clause = list(map(int, input().split()))
        flag = 1
        for literal in clause[1:]:
            x = abs(literal)
            req = 1 if literal < 0 else 0
            if ans[x] == -1: ans[x] = req
            elif ans[x] != req:
                flag = 0; break
        if flag:
            print('YES')
            for i in range(1, n+1): print(0, end=' ') if ans[i] == -1 else print(ans[i], end=' ')
            return 0
        for literal in clause[1:]: ans[abs(literal)] = -1
        m -= 1
    print('NO')
    return 0
if __name__ == '__main__':
    sys.exit(main())