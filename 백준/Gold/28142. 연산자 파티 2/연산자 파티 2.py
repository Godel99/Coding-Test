import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    p = 1000000007
    n = int(input())
    l = n - n % 255
    x = 0
    for i in range(l, n+1):
        x -= i
        x = abs(x)
        if i % 3 == 0: x = (x * i) % p
        if i % 15 == 0: x &= i
        if i % 63 == 0: x ^= i
        if i % 255 == 0: x |= i
        if i % 1023 == 0: x = (x * pow(2, i, p)) % p
    print(x)
    return 0
if __name__ == '__main__':
    sys.exit(main())