from collections import defaultdict, deque

def solution(tickets):
    graph = defaultdict(list)
    
    # 그래프 구성
    for d, a in tickets:
        graph[d].append(a)
    
    # 사전순 경로를 위해 역순 정렬
    for g in graph:
        graph[g].sort(reverse=True)
    
    stack = ['ICN']
    trace = []

    while stack:
        cur = stack[-1]
        if graph[cur]:
            stack.append(graph[cur].pop())
        else:
            trace.append(stack.pop())

    return trace[::-1]


# def solution(tickets):
#     graph = defaultdict(list)
#     for d, a in tickets:
#         graph[d].append(a)

#     for g in graph:
#         graph[g].sort()

#     trace = ['ICN']

#     def DFS(cur):
#         if len(trace) == len(tickets) + 1:
#             return True

#         for i, a in enumerate(graph[cur]):
#             graph[cur].pop(i)
#             trace.append(a)
        
#             if DFS(a):
#                 return True
            
#             trace.pop()
#             graph[cur].insert(i, a)

#         return False

#     DFS('ICN')
                
#     return trace