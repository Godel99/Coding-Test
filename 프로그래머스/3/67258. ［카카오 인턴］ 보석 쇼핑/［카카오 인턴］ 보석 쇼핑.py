def solution(gems):
    from collections import defaultdict

    types_cnt = len(set(gems))

    gems_count = defaultdict(int)
    
    result = [0, len(gems)-1]
    j = 0

    for i in range(len(gems)):
        gems_count[gems[i]] += 1

        while len(gems_count) == types_cnt:
            if i - j < result[1] - result[0]:
                result = [j, i]

            gems_count[gems[j]] -= 1
            if gems_count[gems[j]] == 0:
                del gems_count[gems[j]]
            j += 1

    return [result[0]+1, result[1]+1]