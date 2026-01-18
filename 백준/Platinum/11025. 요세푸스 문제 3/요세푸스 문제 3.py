import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    ans = 1
    for i in range(1, n+1):
        ans = (ans+k-1)%i+1
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())