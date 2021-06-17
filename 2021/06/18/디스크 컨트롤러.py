def solution(jobs):
    import heapq

    jobs.sort(key=lambda j: j[0])
    now, len_job = 0, len(jobs)
    heap = []
    answer = 0
    while jobs or heap:
        while jobs and jobs[0][0] <= now:
            job = jobs.pop(0)
            heapq.heappush(heap, (job[1], job[0]))

        if heap:
            work_h, call_h = heapq.heappop(heap)
            now += work_h
            answer += now - call_h
        else:
            now = jobs[0][0]
    return answer // len_job