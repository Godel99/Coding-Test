# from collections import deque

# def solution(m, n, puddles):
#     maps = [[False] * m for _ in range(n)]
    
#     for i, j in puddles:
#         maps[j - 1][i - 1] = True

#     queue = deque([[0, 0]])
#     cnt = 0

#     while queue:
#         cur = queue.popleft()
#         row, col = cur

#         if cur == [n - 1, m - 1]:
#             cnt += 1
#             continue

#         if col < m - 1:
#             if not maps[row][col + 1]:
#                 queue.append([row, col + 1])
#         if row < n - 1:
#             if not maps[row + 1][col]:
#                 queue.append([row + 1, col])
            
#     return cnt % 1_000_000_007

def solution(m, n, puddles):
    MOD = 1_000_000_007

    puddle = set((y-1, x-1) for x, y in puddles)

    dp = [0] * m
    dp[0] = 1

    for row in range(n):
        for col in range(m):
            if (row, col) in puddle:
                dp[col] = 0
            elif col > 0:
                dp[col] = (dp[col] + dp[col-1]) % MOD

    return dp[m-1]