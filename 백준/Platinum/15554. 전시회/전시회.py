import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from math import inf

def main():
    n = int(input())
    a = sorted(list(map(int, input().split())) for _ in range(n))
    L, R, pres = inf, 0, 0
    for i in range(n):
        L = min(L, pres-a[i][0])
        pres += a[i][1]
        R = max(R, pres-a[i][0]-L)
    print(R)
if __name__ == '__main__':
    main()