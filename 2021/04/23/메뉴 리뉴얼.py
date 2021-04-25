from itertools import combinations

def solution(orders, course):
    order_dict = {}
    answer = []

    for a in course:
        cur_dict = {}
        max_val = 2
        for order in orders:
            for c in combinations(order, a):
                comb = list(c)
                comb.sort()
                cur_order = ''.join(comb)
                cur_dict[cur_order] = cur_dict.get(cur_order, 0) + 1

                if cur_dict[cur_order] > max_val:
                    max_val = cur_dict[cur_order]

        for key, value in cur_dict.items():
            if value == max_val:
                answer.append(key)

    answer.sort()
    return answer