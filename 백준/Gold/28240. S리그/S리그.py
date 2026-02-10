import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a, b, c, d = map(int, input().split())
    ans = []
    for i in range(1, n):
        ans.append(str(i)+' ')
        if i == a or i == b: ans.append('1')
        elif i == c or i == d: ans.append('-1')
        else: ans.append('0')
        ans.append('\n')
    ans.append(str(n)+' ')
    if n == a or n == b: ans.append(str(2*n))
    else: ans.append(str(-2*n))
    print(''.join(ans))
    return 0
if __name__ == '__main__':
    sys.exit(main())