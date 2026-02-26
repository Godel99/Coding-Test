import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    cnt = [0]*10
    l = t = maxl= 0
    for r in range(n):
        cnt[a[r]] += 1
        if cnt[a[r]] == 1: t += 1
        while t > 2:
            cnt[a[l]] -= 1
            if cnt[a[l]] == 0: t -= 1
            l += 1
        maxl = max(maxl, r-l+1)
    print(maxl)
    return 0
if __name__ == '__main__':
    sys.exit(main())