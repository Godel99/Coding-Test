import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += a[i]/max(a)*100
    print(f'{s/n}')
if __name__ == '__main__':
    main()