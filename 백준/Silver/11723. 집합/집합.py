import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    s = set()
    m = int(input())
    for _ in range(m):
        cmd = input().split()
        if len(cmd) == 2: x = int(cmd[1])
        if cmd[0] == "add": s.add(x)
        elif cmd[0] == "remove": s.discard(x)
        elif cmd[0] == "check":
            if x in s: print(1)
            else: print(0)
        elif cmd[0] == "toggle":
            if x in s: s.discard(x)
            else: s.add(x)
        elif cmd[0] == "all": s = set(range(1, 21))
        elif cmd[0] == "empty": s.clear()
    return 0
if __name__ == '__main__':
    sys.exit(main())