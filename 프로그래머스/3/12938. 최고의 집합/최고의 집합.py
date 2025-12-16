# def solution(n, s):
#     if s < n:
#         return [-1]
    
#     q = s // n
#     r = s % n

#     result = [q] * n

#     for i in range(1,r+1):
#         result[-i]+=1

#     return result

def solution(n, s):
    if s < n:
        return [-1]
    
    q = s // n
    r = s % n
    
    return [q] * (n - r) + [q + 1] * r