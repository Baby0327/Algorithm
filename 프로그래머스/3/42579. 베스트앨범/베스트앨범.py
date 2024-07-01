def solution(genres, plays):
    # 장르별 총 플레이타임 저장
    plays_by_genres = {}
    # 장르별 노래의 [번호, 플레이타임] 저장
    info_by_genres = {}

    for i in range(len(genres)):
        plays_by_genres[genres[i]] = plays_by_genres.get(genres[i], 0) + plays[i]
        info_by_genres[genres[i]] = info_by_genres.get(genres[i], []) + [[i, plays[i]]]
    
    # 총 플레이타임 기준 내림차순으로 장르 정렬
    top_genres = sorted(plays_by_genres.items(), key = lambda x : -x[1])
    result = []
    
    for i in top_genres:
        # 플레이타임 기준 내림차순, 같다면 번호 기준 오름차순으로 노래 정렬
        top_music = sorted(info_by_genres[i[0]], key = lambda x : (-x[1], x[0]))
        count = 0
        for j in top_music:
            result.append(j[0])
            count += 1
            # 이미 2곡이 수록된 장르 처리
            if count == 2:
                break
        
    return result