import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    cnt = i = 0
    while cnt < n:
        s = 666+i; i += 1
        if '666' in str(s): cnt += 1  
    print(s)
    return 0
if __name__ == '__main__':
    sys.exit(main())