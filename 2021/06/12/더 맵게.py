def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    answer = 0
    while scoville:
        if scoville[0] < K:
            if len(scoville) == 1:
                answer = -1
                break
            answer += 1
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        else:
            break

    return answer