import sys

input=sys.stdin.readline

def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    for a in A:
        if a < x:
            sys.stdout.write(f'{a} ')

if __name__ == '__main__':
    main()