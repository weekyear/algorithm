def solution(str1, str2):
    ch_dict = {}

    for s1 in range(len(str1) - 1):
        cur_ch = str1[s1:s1 + 2].upper()
        if cur_ch.isalpha():
            if not ch_dict.get(cur_ch, False):
                ch_dict[cur_ch] = [0, 0]
            ch_dict[cur_ch][0] = ch_dict.get(cur_ch)[0] + 1
    for s2 in range(len(str2) - 1):
        cur_ch = str2[s2:s2 + 2].upper()
        if cur_ch.isalpha():
            if not ch_dict.get(cur_ch, False):
                ch_dict[cur_ch] = [0, 0]
            ch_dict[cur_ch][1] = ch_dict.get(cur_ch)[1] + 1

    A, B = 0, 0
    for elem in ch_dict.values():
        A += min(elem)
        B += max(elem)

    return int((A / B) * 65536) if B != 0 else 65536