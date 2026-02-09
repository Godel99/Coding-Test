import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    k = int(input())
    st = []
    for _ in range(k):
        x = int(input())
        if x: st.append(x)
        else: st.pop()
    print(sum(st))
    return 0
if __name__ == '__main__':
    sys.exit(main())