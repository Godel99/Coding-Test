def solution(genres, plays):
    from collections import defaultdict # 딕셔너리 초기화를 위한 라이브러리

    genre_play_sum = defaultdict(int)   # 딕셔너리 값을 0으로 초기화 {장르: 총 플레이 수}
    songs = defaultdict(list)           # 딕셔너리 값을 []으로 초기화 {장르: (플레이 수, 고유번호)}

    for idx, (g, p) in enumerate(zip(genres, plays)): # (장르, 플레이 수) -> [인덱스, (장르, 플레이 수)]
        genre_play_sum[g] += p
        songs[g].append((p, idx))
    
    genre_play_sorted = sorted(genre_play_sum, key = lambda x: genre_play_sum[x], reverse=True) # 총 플레이 수로 내림정렬, 예제에선 [pop, classic]
    
    result = []

    for genre in genre_play_sorted: # [pop, classic]
        songs_sorted = sorted(songs[genre], key = lambda x: (-x[0], x[1]))  # 튜플로 여러가지 정렬 조건 설정, 첫 조건은 플레이 수 순으로, 다음은 고유번호 순
        result.extend(idx for (_, idx) in songs_sorted[:2]) # 슬라이스를 이용해 2곡의 고유번호를 리스트에 확장하여 추가

    return result
