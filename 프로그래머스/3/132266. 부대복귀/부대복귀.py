from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    result = []

    distance = [-1] * (n + 1)
    distance[destination] = 0
    q = deque([destination])

    while q:
        cur = q.popleft()
        for g in graph[cur]:
            if distance[g] == -1:
                q.append(g)
                distance[g] = distance[cur] + 1
    
    for s in sources:
        result.append(distance[s])
        
    return result