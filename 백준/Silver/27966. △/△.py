import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n = int(input())
    print((n-1)*(n-1))
    for i in range(2, n+1): print(1, i)
if __name__ == '__main__':
    main()