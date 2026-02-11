import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from math import sqrt

def main():
    m, n = map(int, input().split())
    p = [True]*(n+1); p[0] = p[1] = False
    for i in range(2, int(sqrt(n))+1):
        if p[i]: 
            for j in range(i*i, n+1, i): p[j] = False
    for i in range(m, n+1):
        if p[i]: print(i)
    return 0
if __name__ == '__main__':
    sys.exit(main())