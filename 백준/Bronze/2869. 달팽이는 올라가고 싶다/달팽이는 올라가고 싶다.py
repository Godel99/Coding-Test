import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b, v = map(int, input().split())
    print((v-b-1)//(a-b)+1)
    return 0
if __name__ == '__main__':
    sys.exit(main())