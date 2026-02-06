import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    A = sorted([(a, i+1) for i, a in enumerate((map(int, input().split())))])
    for i in range(n): 
        if A[i][0] > i//2: return int(not print(-1))
    for i in range(0, n-2, 2): print(A[i][1], A[i+2][1])
    print(A[n-2][1], A[n-1][1])
    for i in range(n-2 if n%2 else n-1, 1, -2): print(A[i][1], A[i-2][1])
    return 0
if __name__ == '__main__':
    sys.exit(main())