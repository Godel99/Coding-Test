import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    if n == 4 or n == 7: return int(not print(-1))
    q, r = divmod(n, 5)
    if r == 0: print(q)
    elif r == 1 or r == 3: print(q + 1)
    else: print(q + 2)
    return 0
if __name__ == '__main__':
    sys.exit(main())