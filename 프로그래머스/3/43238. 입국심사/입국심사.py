def solution(n, times):
    left = min(times)
    result = right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        m = sum(mid // t for t in times)

        if m < n:
            left = mid + 1
        else:
            result = mid
            right = mid - 1
    
    return result