def solution(skill, skill_trees):
    skill_order = [0 for _ in range(26)]
    for s in range(len(skill)):
        skill_order[ord(skill[s]) - 65] = s + 1
    answer = 0
    for skill_tree in skill_trees:
        cur_skill_num = 1
        for skill in skill_tree:
            if skill_order[ord(skill) - 65]:
                if cur_skill_num != skill_order[ord(skill) - 65]:
                    break
                else:
                    cur_skill_num += 1
        else:
            answer += 1

    return answer