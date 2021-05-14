def solution(code, day, data):
    temp = []
    for d in data:
        cur_price, cur_code, cur_time = d.split()
        if cur_code[5:] == code and cur_time[5:13] == day:
            temp.append(d)

    temp.sort(key=lambda a: a[len(a)-2:len(a)])
    answer = []
    for t in temp:
        answer.append(int(t.split()[0][6:]))

    return answer


print(solution("012345", "20190620", ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]))