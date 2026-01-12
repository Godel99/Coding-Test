import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    s = input()
    ans = 0
    for c in s: ans += (1 if int(c) & 1 else -1)
    print(-1+2*(ans>0)+(ans<0))
if __name__ == '__main__':
    main()