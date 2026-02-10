import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import deque

def main():
    n = int(input())
    dq = deque()
    ans = []
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'push': dq.append(int(cmd[1]))
        elif cmd[0] == 'pop': ans.append(dq.popleft() if dq else -1)
        elif cmd[0] == 'size': ans.append(len(dq))
        elif cmd[0] == 'empty': ans.append(0 if dq else 1)
        elif cmd[0] == 'front': ans.append(dq[0] if dq else -1)
        elif cmd[0] == 'back': ans.append(dq[-1] if dq else -1)
    print('\n'.join(map(str, ans))+'\n')
    return 0
if __name__ == '__main__':
    sys.exit(main())