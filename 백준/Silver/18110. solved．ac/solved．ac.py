import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    if not n: return int(not print(0))
    sc = sorted([int(input()) for _ in range(n)])
    exc = int(n*0.15+0.5)
    vsc = sc[exc:n-exc]
    if vsc: print(int(sum(vsc)/len(vsc)+0.5))
    else: print(0)
    return 0
if __name__ == '__main__':
    sys.exit(main())