from copy import deepcopy


def solution(info, query):
    answer = []
    soul_foods = {'chicken': {}, 'pizza': {}}
    careers = {'junior': {}, 'senior': {}}
    parts = {'backend': {}, 'frontend': {}}
    langs = {'cpp': {}, 'java': {}, 'python': {}}

    for c in careers:
        careers[c] = deepcopy(soul_foods)
    for p in parts:
        parts[p] = deepcopy(careers)
    for lang in langs:
        langs[lang] = deepcopy(parts)
    for i in info:
        details = i.split()
        lang = langs.get(details[0])
        part = lang.get(details[1])
        career = part.get(details[2])
        food = career.get(details[3])
        food[details[4]] = food.get(details[4], 0) + 1

    querys = []
    for q in query:
        que = q.split(' and ')
        last = que.pop()
        for l in last.split():
            que.append(l)
        querys.append(que)

    for que in querys:
        result = 0
        q_langs = []
        if que[0] == '-':
            for lang in langs.values():
                if len(lang):
                    q_langs.append(lang)
        else:
            cur_lang = langs.get(que[0])
            if len(cur_lang):
                q_langs.append(cur_lang)

        q_parts = []
        if que[1] == '-':
            for q_lang in q_langs:
                for p in q_lang.values():
                    if len(p):
                        q_parts.append(p)
        else:
            for q_lang in q_langs:
                cur_part = q_lang.get(que[1])
                if len(cur_part):
                    q_parts.append(cur_part)

        q_careers = []
        if que[2] == '-':
            for q_part in q_parts:
                for p in q_part.values():
                    if len(p):
                        q_careers.append(p)
        else:
            for q_part in q_parts:
                cur_career = q_part.get(que[2])
                if len(cur_career):
                    q_careers.append(cur_career)

        q_foods = []
        if que[3] == '-':
            for q_career in q_careers:
                for p in q_career.values():
                    if len(p):
                        q_foods.append(p)
        else:
            for q_career in q_careers:
                cur_food = q_career.get(que[3])
                if len(cur_food):
                    q_foods.append(cur_food)

        print(q_foods)
        cur_num = 0
        for food in q_foods:
            for score, num in food.items():
                criteria = que[4]
                if score >= criteria:
                    cur_num += 1

        answer.append(cur_num)

    return answer

solution(
["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
)