def solution(w, h):
    def get_gcd(w, h):
        while w != h:
            if w > h:
                w = w - h
            else:
                h = h - w
        return w

    del_num = 0
    max_mod = get_gcd(w, h)
    if w == 1 or h == 1:
        return 0

    pre = 0
    for s in range(1, w // max_mod + 1):
        nxt = h / w * s
        ans_nxt = int(nxt) + 1 if nxt > int(nxt) else int(nxt)
        del_num += ans_nxt - int(pre)
        pre = nxt

    answer = w * h - del_num * max_mod
    return answer