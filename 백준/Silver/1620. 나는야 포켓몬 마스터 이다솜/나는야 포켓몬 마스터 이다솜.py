import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    pdex_name = {}
    pdex_id = ['']*(n+1)
    ans = []
    for i in range(1, n+1):
        name = input()
        pdex_name[name] = str(i)
        pdex_id[i] = name
    for _ in range(m):
        q = input()
        if q.isdigit(): ans.append(pdex_id[int(q)])
        else: ans.append(pdex_name[q])
    print('\n'.join(ans))
    return 0
if __name__ == '__main__':
    sys.exit(main())