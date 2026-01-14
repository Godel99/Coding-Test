import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def recursion(s, l, r):
    if l >= r: return 1, l+1
    elif s[l] != s[r]: return 0, l+1
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

def main():
    n = int(input())
    for _ in range(n):
        s = input()
        print(isPalindrome(s)[0], isPalindrome(s)[1])
if __name__ == '__main__':
    main()