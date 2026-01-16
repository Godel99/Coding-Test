import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**7)

def main():
    n = int(input())
    out = []
    def hanoi(d, start, via, end):
        if d == 1:
            out.append(f'{start} {end}')
            return
        hanoi(d-1, start, end, via)
        out.append(f'{start} {end}')
        hanoi(d-1, via, start, end)
    print((1 << n)-1)
    hanoi(n, 1, 2, 3)
    print('\n'.join(out))
if __name__ == '__main__':
    main()