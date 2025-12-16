# def solution(routes):
#     n = len(routes)
#     seen = [0] * n

#     for i in range(n):
#         start, end = routes[i]
#         for j in range(n):
#             if i == j:
#                 continue
#             t_start, t_end = routes[j]
#             if (start <= t_start <= end or start <= t_end <= end):
#                 seen[i] += 1
                
#     cnt = 0  

#     for i in range(n):
#         if seen[i] == 1:
#             start, end = routes[i]
#             for j in range(n):
#                 if i == j:
#                     continue
#                 t_start, t_end = routes[j]
#                 if (start <= t_start <= end or start <= t_end <= end):
#                     if seen[j] != 0:
#                         cnt += 1
#         elif seen[i] == 0:
#             cnt += 1                
    
#     return cnt
#   실패한 코드

def solution(routes):
    routes_sorted = sorted(routes, key=lambda x: x[1])

    cnt = 1
    end = routes_sorted[0][1]

    for s, e in routes_sorted[1:]:
        if s > end:
            cnt += 1
            end = e
    
    return cnt