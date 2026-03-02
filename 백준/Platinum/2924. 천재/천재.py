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
    m = 1; s = set()
    for i in range(c+1, n-d+1):
        r = find(i)
        if r in s: continue
        s.add(r)
        m = lcm(m, -par[r])
        if m > b: m = b+1; break
    print((b+m-1)//m - (a+m-2)//m)
if __name__ == '__main__':
    main()