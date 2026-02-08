import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    data = sys.stdin.read().splitlines()
    for s in data:
        if s == '.': break
        stack = []
        flag = 1
        for c in s:
            if c == '.': break
            if c == '(' or c == '[': stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(': flag = 0; break
            elif c == ']':
                if not stack or stack.pop() != '[': flag = 0; break
        if flag and not stack: print('yes')
        else: print('no')
    return 0
if __name__ == '__main__':
    sys.exit(main())
