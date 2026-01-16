import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = [0]+list(map(int, input().split()))
    cnt = 0
    for i in range(1, n+1):
        if a[i] == i:
            cnt += 1
            a[i] = 1+(i==1)
    print(cnt)
    print(*a[1:])
if __name__ == '__main__':
    main()