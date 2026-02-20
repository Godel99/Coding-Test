import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from math import sqrt

def main():
    n = int(input())
    if n == int(sqrt(n))**2: return int(not print(1))
    for i in range(1, int(sqrt(n))+1):
        if n-i*i == int(sqrt(n-i*i))**2: return int(not print(2))
    for i in range(1, int(sqrt(n))+1):
        for j in range(1, int(sqrt(n-i*i))+1):
            if n-i*i-j*j == int(sqrt(n-i*i-j*j))**2: return int(not print(3))
    print(4)
    return 0
if __name__ == '__main__':
    sys.exit(main())