import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    for _ in range(m):
        x, y = map(int, input().split())
        edge[x].append(y)
        edge[y].append(x)
    ans = 0
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            st = [i]
            ans += 1
            while st:
                cur = st.pop()
                for nxt in edge[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        st.append(nxt)
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())