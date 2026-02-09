import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    st = []
    idx = 1
    ans = []
    for _ in range(n):
        com = data[idx]; idx +=1
        if com == 'push': st.append(data[idx]); idx += 1
        elif com == 'pop': ans.append(st.pop() if st else -1)
        elif com == 'size': ans.append(len(st))
        elif com == 'empty': ans.append(0 if st else 1)
        elif com == 'top': ans.append(st[-1] if st else -1)
    print('\n'.join(map(str, ans))+'\n')
    return 0
if __name__ == '__main__':
    sys.exit(main())