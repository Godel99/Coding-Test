import sys

input=sys.stdin.readline

def main():
    n = int(input())
    if 90 <= n <= 100:
        sys.stdout.write('A')
    elif 80 <= n < 90:
        sys.stdout.write('B')
    elif 70 <= n < 80:
        sys.stdout.write('C')
    elif 60 <= n < 70:
        sys.stdout.write('D')
    else:
        sys.stdout.write('F')

if __name__ == '__main__':
    main()