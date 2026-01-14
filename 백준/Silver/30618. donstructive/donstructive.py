import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    for i in range(1, n+1, 2): print(i, end=' ')
    for i in range(n-n%2, 0, -2): print(i, end=' ')
if __name__ == '__main__':
    main()