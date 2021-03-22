samples = ["AaTa+!12-3)))))", "aaaaZZZZ)))))", "CaCbCgCdC888834A", "UUUUU", "ZzZz9Z824"]

def solution(inp_str):
    rules = [0 for _ in range(6)]
    chr_types = [0 for _ in range(4)]
    num_types = 0
    if not 8 <= len(inp_str) <= 15:
        rules[1] = 1

    chars = [False for _ in range(127)]
    num_chars = {}
    for i in range(65, 91):
        chars[i] = True
    for i in range(97, 123):
        chars[i] = True
    for i in range(48, 58):
        chars[i] = True
    for i in "~!@#$%^&*":
        chars[ord(i)] = True

    prev = ''
    prev_stack = 1
    for cur_ch in inp_str:
        if prev == cur_ch:
            prev_stack += 1
            if prev_stack > 3:
                rules[4] = 1
        else:
            prev_stack = 1
        prev = cur_ch

        num_chars[cur_ch] = num_chars.get(cur_ch, 0) + 1
        if num_chars.get(cur_ch, 0) > 4:
            rules[5] = 1

        if not chars[ord(cur_ch)]:
            rules[2] = 1
        else:
            if 65 <= ord(cur_ch) < 91:
                if not chr_types[0]:
                    chr_types[0] = 1
                    num_types += 1
            elif 97 <= ord(cur_ch) < 123:
                if not chr_types[1]:
                    chr_types[1] = 1
                    num_types += 1
            elif 48 <= ord(cur_ch) < 58:
                if not chr_types[2]:
                    chr_types[2] = 1
                    num_types += 1
            else:
                if not chr_types[3]:
                    chr_types[3] = 1
                    num_types += 1

    if num_types < 3:
        rules[3] = 1

    answer = []
    for r in range(1, len(rules)):
        if rules[r]:
            answer.append(r)
    if not answer:
        answer.append(0)
    return answer

for sample in samples:
    print(solution(sample))