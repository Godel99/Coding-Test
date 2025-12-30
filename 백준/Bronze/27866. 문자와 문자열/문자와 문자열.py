import sys

input=sys.stdin.readline

def main():
    S = input()
    i = int(input())

    sys.stdout.write(S[i-1])
 
if __name__ == '__main__':
    main()