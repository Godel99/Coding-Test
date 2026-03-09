import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n, k = map(int, input().split())
    print('YES')
    for i in range(1, k): print(i, end=' ')
    for i in range(n, k-1, -1): print(i, end=' ')
if __name__ == '__main__':
    main()