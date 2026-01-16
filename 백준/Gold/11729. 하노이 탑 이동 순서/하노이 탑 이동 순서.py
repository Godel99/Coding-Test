import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()
    
def main():
    n = int(input())
    def hanoi(d, start, via, end):
        if d == 1:
            return print(start, end)
        hanoi(d-1, start, end, via)
        print(start, end)
        hanoi(d-1, via, start, end)
    print(pow(2, n)-1)
    hanoi(n, 1, 2, 3)
if __name__ == '__main__':
    main()