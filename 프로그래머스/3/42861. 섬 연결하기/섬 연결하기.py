def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        ra = find(a)
        rb = find(b)

        if ra == rb:
            return False
        
        parent[rb] = ra
        return True
    
    total_cost = 0
    edges_cnt = 0

    for a, b, cost in costs:
        if union(a, b):
            total_cost += cost
            edges_cnt += 1
            if edges_cnt == n - 1:
                break
    
    return total_cost