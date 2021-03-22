samples = [
    ["line", ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"], ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]],
    ["bank", ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]]
]

answer = [
    [True, False],
    [False, False]
]

def solution(program, flag_rules, commands):
    def convert_flag_rules_string_to_dict(f_rules):
        flag_rules_temp = {}
        aliases_temp = {}
        for flag_rule in f_rules:
            cur_flag_rule = flag_rule.split()
            flag_name, flag_argument_type = cur_flag_rule[0], cur_flag_rule[1]
            # dict_rules에 flag의 이름을 key로 타입을 value로 넣어준다.
            flag_rules_temp[flag_name] = flag_argument_type
            # 타입이 ALIAS일 경우 aliases_temp에 alias를 key로 원래 이름을 value로 넣어준다.
            if flag_argument_type == "ALIAS":
                aliases_temp[flag_name] = cur_flag_rule[2]

        return flag_rules_temp, aliases_temp

    def check_argument_validation(arg_type, arg_values):
        if arg_type == "NUMBER":
            # 개수가 2 이상이거나 숫자가 아닐 경우 False를 반환
            if len(arg_values) > 1 or not arg_values[0].isdigit():
                return False
        elif arg_type == "STRING":
            # 개수가 2 이상이거나 알파벳이 아닐 경우 False를 반환
            if len(arg_values) > 1 or not arg_values[0].isalpha():
                return False
        elif arg_type == "NUMBERS":
            for cur_flag_argument in arg_values:
                if not cur_flag_argument.isdigit():
                    return False
        elif arg_type == "STRINGS":
            for cur_flag_argument in arg_values:
                if not cur_flag_argument.isalpha():
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

            # 타입이 만약에 "ALIAS"라면 cur_arg_type을 원래 이름으로 바꾼다.
            if cur_arg_type == "ALIAS":
                cur_arg_type = dict_rules.get(aliases[command_parts[idx]])

            # flag 사용 횟수를 업데이트한다. 이미 사용했다면 False를 반환한다.
            count_flags[cur_arg_type] = count_flags.get(cur_arg_type, 0) + 1
            if count_flags[cur_arg_type] > 1:
                return False

            if cur_arg_type != 'NULL':
                cur_flag_arguments = []
                # 다음 타입이 나올 때까지 인자들을 골라낸다.
                while not dict_rules.get(command_parts[idx + 1], False):
                    cur_flag_arguments.append(command_parts[idx + 1])
                    idx += 1
                    # 인덱스를 초과하면 멈춘다.
                    if idx + 1 >= len_part:
                        break

                if not check_argument_validation(cur_arg_type, cur_flag_arguments):
                    return False

            idx += 1
        else:
            return True

    dict_rules, aliases = convert_flag_rules_string_to_dict(flag_rules)
    answer = []
    for c in commands:
        answer.append(check_command_validation(program, c))
    return answer

for sample in samples:
    print(solution(sample[0], sample[1], sample[2]))