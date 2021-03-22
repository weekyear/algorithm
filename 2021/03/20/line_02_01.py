samples = [
    ["line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"]],
    ["line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"]]
]

answer = [
    [True, False],
    [False, False]
]



def solution(program, flag_rules, commands):
    def convert_flag_rules_string_to_dict(f_rules):
        flag_rules_temp = {}
        for flag_rule in f_rules:
            cur_flag_rule = flag_rule.split()
            flag_name, flag_argument_type = cur_flag_rule[0], cur_flag_rule[1]
            # dict_rules에 flag의 이름을 key로 타입을 value로 넣어준다.
            flag_rules_temp[flag_name] = flag_argument_type

        return flag_rules_temp

    def check_argument_validation(arg_type, arg_value):
        if arg_type == "NUMBER":
            if not arg_value.isdigit():
                return False
        elif arg_type == "STRING":
            if not arg_value.isalpha():
                return False
        return True

    def check_command_validation(program_name, command):
        command_parts = command.split()
        len_part = len(command_parts)
        if command_parts[0] != program_name:
            return False

        # flag가 중복되는지 확인하는 dict를 생성한다.
        count_flags = {}
        idx = 1
        while idx < len_part:
            # 현재 idx의 타입을 가져온다. 해당하는 타입이 없다면 False를 넣어준다.
            cur_arg_type = dict_rules.get(command_parts[idx], False)

            # 현재 idx의 타입이 존재하지 않는다는 말은 실제로 올바르지 않은 타입을 기입했거나
            # 인수 개수를 부적절하게 기입하였다는 의미이므로 False를 반환한다.
            if not cur_arg_type:
                return False

            # flag 사용 횟수를 업데이트한다. 이미 사용했다면 False를 반환한다.
            count_flags[cur_arg_type] = count_flags.get(cur_arg_type, 0) + 1
            if count_flags[cur_arg_type] > 1:
                return False

            if cur_arg_type != 'NULL':
                idx += 1
                cur_flag_argument = command_parts[idx]
                if not check_argument_validation(cur_arg_type, cur_flag_argument):
                    return False

            idx += 1
        else:
            return True

    # flag_rules를 dict형식으로 정리한다.
    dict_rules = convert_flag_rules_string_to_dict(flag_rules)
    answer = []
    # 각 command를 순회하여 유효한지 검사한다.
    for c in commands:
        answer.append(check_command_validation(program, c))
    return answer

for sample in samples:
    print(solution(sample[0], sample[1], sample[2]))