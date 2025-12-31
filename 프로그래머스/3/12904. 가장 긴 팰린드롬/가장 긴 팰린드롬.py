def solution(s):
    n = len(s)
    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    max_len = 1
    for i in range(n):
        odd_len = expand(i, i)
        even_len = expand(i, i+1)

        max_len = max(max_len, odd_len, even_len)

    return max_len


# def solution(s):
#     n = len(s)
#     length = 1
#     idx = 0

#     for idx in range(n):
#         if idx + 1 < n and s[idx] == s[idx+1]:
#             left = idx
#             right = idx + 1
#             while left >= 0 and right < n and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             length = max(length, (right - left - 1))

#         if idx - 1 >= 0 and idx + 1 < n and s[idx-1] == s[idx+1]:
#             left = idx - 1
#             right = idx + 1
#             while left >= 0 and right < n and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             length = max(length, (right - left - 1))
        
#     return length
        