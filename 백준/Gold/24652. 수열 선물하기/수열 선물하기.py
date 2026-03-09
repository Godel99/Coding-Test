import sys 
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    print('YES')
    for i in range(1, k): print(i, end=' ')
    for i in range(n, k-1, -1): print(i, end=' ')
if __name__ == '__main__':
    main()