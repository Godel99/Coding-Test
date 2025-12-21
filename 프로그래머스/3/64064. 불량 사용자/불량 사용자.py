def solution(user_id, banned_id):
    def is_match(user, banned):
        if len(user) != len(banned):
            return False
        return all(b == '*' or b == u for u, b in zip(user, banned))

    pattern_id = []
    for banned in banned_id:
        pattern = [user for user in user_id if is_match(user, banned)]
        pattern_id.append(pattern)

    result = set()
    chosen = set()

    def DFS(depth):
        if depth == len(pattern_id):
            result.add(frozenset(chosen))
            return
        
        for id in pattern_id[depth]:
            if id not in chosen:
                chosen.add(id)
                DFS(depth+1)
                chosen.remove(id)

    DFS(0)

    return len(result)