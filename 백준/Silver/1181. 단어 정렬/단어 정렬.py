import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    ans = list(set(input() for _ in range(n)))
    ans.sort(key=lambda x: (len(x), x))
    print(*ans, sep='\n')
    return 0
if __name__ == '__main__':
    sys.exit(main())