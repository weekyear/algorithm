def solution(genres, plays):
    total_plays = {}
    album = {}
    for g in range(len(genres)):
        if not album.get(genres[g], False):
            album[genres[g]] = []
        album[genres[g]].append((g, plays[g]))
        total_plays[genres[g]] = total_plays.get(genres[g], 0) + plays[g]

    lst_plays = [(key, val) for key, val in total_plays.items()]
    lst_plays.sort(key=lambda p: -p[1])

    answer = []
    for genre, play in lst_plays:
        album[genre].sort(key=lambda song: (-song[1], song[0]))
        answer.append(album[genre][0][0])
        if len(album[genre]) > 1:
            answer.append(album[genre][1][0])

    return answer