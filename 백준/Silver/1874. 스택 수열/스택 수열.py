import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    st = []
    ans = []
    nx = 1
    for _ in range(n):
        x = int(input())
        while nx <= x:
            ans.append('+')
            st.append(nx); nx += 1
        if st and st[-1] == x: 
            ans.append('-')
            st.pop()
        else: return int(not print('NO'))
    print('\n'.join(ans))
    return 0
if __name__ == '__main__':
    sys.exit(main())