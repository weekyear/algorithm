# import sys
# sys.stdin = open('input_line_01.txt', 'r')

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

def solution(table, languages, preference):
    jobs = []
    scoresByJob = {}

    for i in range(5):
        info_split = [a for a in table[i].split()]
        job = info_split[0]
        jobs.append(job)
        for j in range(1, 6):
            scoresByJob[(job, info_split[j])] = 6 - j

    max_res = 0
    answer = ''
    for job in jobs:
        cur_res = 0
        for l in range(len(languages)):
            cur_res += scoresByJob.get((job, languages[l]), 0) * preference[l]
        if cur_res > max_res:
            max_res = cur_res
            answer = job
        elif cur_res == max_res:
            answer = min(job, answer)

    return answer

print(solution(table, languages, preference))