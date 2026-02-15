import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    dic = {}
    for _ in range(n):
        site, pw = input().split()
        dic[site] = pw
    for _ in range(m): print(dic[input()])
    return 0
if __name__ == '__main__':
    sys.exit(main())