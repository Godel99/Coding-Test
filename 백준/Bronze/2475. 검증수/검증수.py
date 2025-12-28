import sys

input=sys.stdin.readline

def main():
    N = list(map(int, input().split()))

    sumn = 0 
    for n in N:
        sumn += n**2

    sys.stdout.write(str(sumn % 10))

if __name__ == '__main__':
    main()