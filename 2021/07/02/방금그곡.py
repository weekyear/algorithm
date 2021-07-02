def convert_to_melody(_music):
    lst = []
    for m in _music:
        if m == '#':
            lst[len(lst) - 1] = lst[len(lst) - 1] + '#'
        else:
            lst.append(m)
    return lst


def solution(music, musicinfos):
    answer = [0, '(None)']

    music = convert_to_melody(music)
    len_music = len(music)

    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        melody = convert_to_melody(melody)
        len_melody = len(melody)
        s_h, s_m = map(int, start.split(':'))
        e_h, e_m = map(int, end.split(':'))
        length = (e_h - s_h) * 60 + (e_m - s_m)
        for m in range(len_melody):
            if melody[m] == music[0]:
                for n in range(1, len_music):
                    if m + n + 1 > length or music[n] != melody[(m + n) % len_melody]:
                        break
                else:
                    if length > answer[0]:
                        answer = [length, title]
                    break

    return answer[1]