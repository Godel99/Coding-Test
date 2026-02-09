import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        st = []
        flag = 1
        for c in s:
            if c == '(': st.append(c)
            elif st: st.pop()
            else: flag = 0; break
        if flag and not st: print('YES')
        else: print('NO')
    return 0
if __name__ == '__main__':
    sys.exit(main())