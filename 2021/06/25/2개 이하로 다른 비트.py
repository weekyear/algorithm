def solution(numbers):
    answer = []
    for number in numbers:
        binary = list(bin(number))
        for i in range(len(binary) - 1, 1, -1):
            if binary[i] == "0":
                c = i
                binary[c] = "1"
                break
        else:
            c = 2
            binary.insert(2, "1")

        if c != len(binary) - 1:
            binary[c + 1] = "0"
        answer.append(int(''.join(binary), 2))
    return answer