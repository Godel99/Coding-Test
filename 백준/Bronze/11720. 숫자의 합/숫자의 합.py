import sys

input=sys.stdin.readline

def main():
    n = int(input())
    s = input()
    total = 0
    for i in range(len(s)-1):
        total += int(s[i])
    
    sys.stdout.write(str(total))
    
if __name__ == '__main__':
    main()