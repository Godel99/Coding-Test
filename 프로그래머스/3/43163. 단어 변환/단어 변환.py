from collections import deque
import heapq as hq
import copy

# def solution(begin, target, words):
#     if target not in words:
#         return 0
    
#     n = len(words)
#     queue = deque()
#     passed = []

#     for i in range(n):
#         if CHD(begin, words[i]) == 1:
#             queue.append((i, passed))

#     if not queue:
#         return 0

#     distance = []

#     while queue:
#         node, passed = queue.pop()
#         passed_cy = copy.deepcopy(passed)
#         passed_cy.append(node)
    
#         if words[node] == target:
#             cnt = len(passed_cy)
#             hq.heappush(distance, cnt)
#             continue
            
#         for i in range(n):
#             if CHD(words[i], words[node]) == 1 and i not in passed:
#                 queue.append((i, passed_cy))
#     return hq.heappop(distance)

# def CHD(word1 :str, word2: str):
#     return sum(char1 != char2 for char1, char2 in zip(word1, word2))

def CHD(word1 :str, word2: str) -> int:
    return sum(char1 != char2 for char1, char2 in zip(word1, word2))

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        cur, cnt = queue.popleft()

        if cur == target:
            return cnt
        
        for word in words:
            if word not in visited and CHD(word, cur) == 1:
                visited.add(word)
                queue.append((word, cnt + 1))

    return 0

