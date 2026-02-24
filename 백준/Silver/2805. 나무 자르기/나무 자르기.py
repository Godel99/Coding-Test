import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n, m = map(int, input().split())
    tree = tuple(map(int, input().split()))
    low = 0
    high = max(tree)
    while low <= high:
        mid = (low+high)//2
        total = sum(t - mid for t in tree if t > mid)
        if total >= m: low = mid+1
        else: high = mid-1
    print(high)
    return 0
if __name__ == '__main__':
    sys.exit(main())