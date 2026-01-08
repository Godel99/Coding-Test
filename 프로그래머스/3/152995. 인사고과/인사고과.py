def solution(scores):
    sorted_scores = sorted(scores, key = lambda x: (-x[0], x[1]))
    wanho = tuple(scores[0])
    wanho_sum = sum(wanho)
    maxs = -1
    rank = 1
    for f, s in sorted_scores:
        if s < maxs:
            if (f, s) == wanho:
                return -1
            continue

        maxs = s
        
        if f + s > wanho_sum:
            rank += 1

    return rank
