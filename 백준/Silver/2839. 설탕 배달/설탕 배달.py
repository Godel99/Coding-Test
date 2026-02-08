import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    ans = 0
    while n >= 0:
        if n % 5 == 0:
            ans += (n//5)
            print(ans)
            break
        n -= 3
        ans += 1
    else: print(-1)
    return 0
if __name__ == '__main__':
    sys.exit(main())