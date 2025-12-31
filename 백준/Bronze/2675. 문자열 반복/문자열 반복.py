import sys

def main():
    T = int(input())
   
    for _ in range(T):
        n, text = input().split()
        n = int(n)
        for c in text:
            for i in range(n):
                sys.stdout.write(c)
        sys.stdout.write('\n')

if __name__ == '__main__':
    main()