def solution(numbers, hand):
    left, right = '*', '#'
    answer = []
    num_dict = {1: 'L', 2: {1: 1, 2: 0, 3: 1, 4: 2, 5: 1, 6: 2, 7: 3, 8: 2, 9: 3, 0: 3, '*': 4, '#': 4}, 3: 'R', 4: 'L',
                5: {1: 2, 2: 1, 3: 2, 4: 1, 5: 0, 6: 1, 7: 2, 8: 1, 9: 2, 0: 2, '*': 3, '#': 3}, 6: 'R', 7: 'L',
                8: {1: 3, 2: 2, 3: 3, 4: 2, 5: 1, 6: 2, 7: 1, 8: 0, 9: 1, 0: 1, '*': 2, '#': 2}, 9: 'R',
                0: {1: 4, 2: 3, 3: 4, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 2, 0: 0, '*': 1, '#': 1}}
    for number in numbers:
        if type(num_dict[number]) == str:
            cur_finger = num_dict[number]
        else:
            if num_dict[number][left] < num_dict[number][right]:
                cur_finger = 'L'
            elif num_dict[number][left] > num_dict[number][right]:
                cur_finger = 'R'
            else:
                cur_finger = hand[0].upper()

        answer.append(cur_finger)
        if cur_finger == 'L':
            left = number
        else:
            right = number

    return ''.join(answer)