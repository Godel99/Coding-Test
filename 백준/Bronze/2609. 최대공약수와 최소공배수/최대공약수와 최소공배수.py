import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b = map(int, input().split())
    def gcd(a, b):
        while b:
            r = a % b
            a = b
            b = r
        return a
    print(g:=gcd(a, b))
    print(a*b // g)
    return 0
if __name__ == '__main__':
    sys.exit(main())