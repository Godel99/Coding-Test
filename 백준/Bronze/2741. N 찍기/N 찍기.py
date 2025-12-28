import sys

input=sys.stdin.readline

def main():
    n = int(input())
    for i in range(1, n+1):
        sys.stdout.write(f'{i}\n')

if __name__ == '__main__':
    main()