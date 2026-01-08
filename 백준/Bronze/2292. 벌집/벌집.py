import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    l = 1; r = 1

    if n == 1:
        print(1)
        return 0
    
    while r < n:
        r += l*6
        l += 1

    print(l)
if __name__ == '__main__':
    main()

