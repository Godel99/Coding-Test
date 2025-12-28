import sys

input=sys.stdin.readline

def main():
    n = int(input())
    for i in range(1, 10):
        sys.stdout.write(f'{n} * {i} = {n*i}\n')

if __name__ == '__main__':
    main()