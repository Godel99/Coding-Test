import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    k = int(input())
    s = [0]+list(map(int, input().split()))
    n = s[-1]
    par = [0]*(n//2+1)
    L = [0]*(n+1); R = [0]*(n+1)
    if s[1] != 0: print(-1); return
    print(n//2)
    for i in range(1, n+1, 2): par[i//2+1] = i
    idx = 2
    for i in range(1, n//2):
        if s[idx] != i*2: par[i], par[i+1] = par[i+1], par[i]
        else: idx += 1
    for i in range(1, n//2+1): L[par[i]], R[par[i]] = par[i-1], i*2
    for i in range(1, n+1, 2): print(L[i], R[i])
if __name__ == '__main__':
    main()