import sys

input=sys.stdin.readline

def main():
    a, b = map(int, input().split())

    sys.stdout.write(str(a/b))

if __name__ == '__main__':
    main()