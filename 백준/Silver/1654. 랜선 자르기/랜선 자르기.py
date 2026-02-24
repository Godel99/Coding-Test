import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    k, n = map(int, input().split())
    line = tuple(int(input()) for _ in range(k))
    low = 1; high = max(line)
    while low <= high:
        mid = (low+high)//2
        total = sum(l//mid for l in line)
        if total >= n: low = mid+1
        else: high = mid-1
    print(high)
    return 0
if __name__ == '__main__':
    sys.exit(main())