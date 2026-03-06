import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque

def main():
    t = int(input())
    for _ in range(t):
        p = input()
        n = int(input())
        x = input()[1:-1]
        if x: dq = deque(x.split(','))
        else: dq = deque()
        flag = True
        for c in p:
            if c == 'R': flag = not flag
            else:
                if dq:
                    if flag: dq.popleft()
                    else: dq.pop()
                else: print('error'); break
        else:
            if not flag: dq.reverse()
            print(f"[{','.join(dq)}]")
if __name__ == '__main__':
    main()