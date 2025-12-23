def solution(stones, k):
    left = 1
    right = max(stones)
    
    while left <= right:
        x_cnt = 0
        mid = (left + right) // 2

        for stone in stones:
            if x_cnt == k:
                break
            if stone <= mid:
                x_cnt += 1
            else:
                x_cnt = 0

        if x_cnt == k:
            right = mid - 1
        else:
            left = mid + 1
    
    return left