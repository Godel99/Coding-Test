import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    print(2 if n&3 == 3 else 1)
    return 0
if __name__ == '__main__':
    sys.exit(main())