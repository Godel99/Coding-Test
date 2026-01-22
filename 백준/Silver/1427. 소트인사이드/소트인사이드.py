import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = input()
    cnt = [0]*10
    for c in n: cnt[int(c)] += 1
    for i in range(9, -1, -1):
        for _ in range(cnt[i]): print(i, end='')
    return 0
if __name__ == '__main__':
    sys.exit(main())