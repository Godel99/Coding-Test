from collections import defaultdict, deque

def solution(tickets):
    graph = defaultdict(list)
    for d, a in tickets:
        graph[d].append(a)

    for g in graph:
        graph[g].sort()

    trace = ['ICN']

    def DFS(cur):
        if len(trace) == len(tickets) + 1:
            return True

        for i, a in enumerate(graph[cur]):
            graph[cur].pop(i)
            trace.append(a)
        
            if DFS(a):
                return True
            
            trace.pop()
            graph[cur].insert(i, a)

        return False

    DFS('ICN')
                
    return trace