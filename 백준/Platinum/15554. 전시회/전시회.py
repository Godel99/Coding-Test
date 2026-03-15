import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from math import inf

def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort()
    L, R, pre= inf, 0, 0
    for i in range(n):
        pres = pre+a[i][1]
        L = min(L, pre-a[i][0])
        R = max(R, pres-a[i][0]-L)
        pre = pres
    print(R)
if __name__ == '__main__':
    main()