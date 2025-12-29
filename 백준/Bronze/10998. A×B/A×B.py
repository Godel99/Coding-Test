import sys

input=sys.stdin.readline

def main():
    a, b = map(int, input().split())
    sys.stdout.write(str(a * b) + '\n')
 
if __name__ == '__main__':
    main()