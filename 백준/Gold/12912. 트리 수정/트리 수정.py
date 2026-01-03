import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    tree = [[] for _ in range(N)]
    edges = []

    for i in range(N-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
        tree[u].append((v, w, i))
        tree[v].append((u, w, i))

    def dfs_farthest(start, blocked_edge):
        visited = [False] * N
        stack = [(start, 0)]
        visited[start] = True

        farthest_node = start
        max_dist = 0

        while stack:
            cur, dist = stack.pop()

            if dist > max_dist:
                max_dist = dist
                farthest_node = cur
            
            for nxt, w, eid in tree[cur]:
                if eid == blocked_edge:
                    continue
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, dist + w))
        
        return (farthest_node, max_dist)
    
    def dfs_diameter(start, blocked_edge):
        x, _ = dfs_farthest(start, blocked_edge)
        _, diameter = dfs_farthest(x, blocked_edge)

        return diameter
    
    answer = 0
    for i in range(N-1):
        u, v, w = edges[i]

        x, _ = dfs_farthest(u, i)
        _, dist_u = dfs_farthest(x, i)
        diam_u = dist_u

        y, _ = dfs_farthest(v, i)
        _, dist_v = dfs_farthest(y, i)
        diam_v = dist_v

        candidate = max(
            diam_u,
            diam_v,
            dist_u + w + dist_v
        )

        answer = max(answer, candidate)
    
    print(answer)
    
if __name__ == '__main__':
    main()