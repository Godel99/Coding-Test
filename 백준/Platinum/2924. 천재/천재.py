import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from math import lcm

def main():
    n, a, b, c, d = map(int, input().split())
    par = [-1]*(n+1)
    def find(x):
        if par[x] < 0: return x
        par[x] = find(par[x])
        return par[x]
    def union(x, y):
        x = find(x); y = find(y)
        if x == y: return
        if par[x] > par[y]: x, y = y, x
        par[x] += par[y]
        par[y] = x
    for i, x in enumerate(list(map(int, input().split()))): union(i+1, x)
    m = 1
    for i in range(c+1, n-d+1): 
        m = lcm(m, -par[find(i)])
        if m > b: break
    print((b+m-1)//m - (a+m-2)//m)
if __name__ == '__main__':
    main()