import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n, m = map(int, input().split())
    if n > m: n, m = m, n
    print('ChongChong' if n == 1 and m == 2 else 'GomGom')
if __name__ == '__main__':
    main()