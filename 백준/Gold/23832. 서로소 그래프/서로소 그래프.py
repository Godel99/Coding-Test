import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    phi = [i for i in range(n+1)]
    for i in range(2, n+1):
        if phi[i] == i:
            for j in range(i, n+1, i):
                phi[j] -= phi[j]//i
    print(sum(phi[2:]))
    return 0
if __name__ == '__main__':
    sys.exit(main())