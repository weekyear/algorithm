def solution(cacheSize, cities):
    from collections import defaultdict
    from collections import deque
    cache_dict = defaultdict(int)
    Q = []
    cur_num, answer = 0, 0
    for city in cities:
        city = city.lower()
        if not cache_dict[city]:
            Q.append(city)
            if len(Q) > cacheSize:
                del_city = Q.pop(0)
                for key in cache_dict.keys():
                    if cache_dict[key] > cache_dict[city]:
                        cache_dict[key] -= 1

            cache_dict[city] = len(Q)
            answer += 5
        else:
            Q.pop(cache_dict[city] - 1)
            for key in cache_dict.keys():
                if cache_dict[key] > cache_dict[city]:
                    cache_dict[key] -= 1
            Q.append(city)
            cache_dict[city] = len(Q)
            answer += 1

    return answer