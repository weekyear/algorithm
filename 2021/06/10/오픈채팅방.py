def solution(records):
    chats = []
    id_dict = {}

    for record in records:
        if record[0] == "L":
            command, uid = record.split()
        else:
            command, uid, nickname = record.split()

        if command == "Enter":
            chats.append((uid, "E"))
            id_dict[uid] = nickname
        elif command == "Leave":
            chats.append((uid, "L"))
        else:
            id_dict[uid] = nickname

    answer = []
    for chat in chats:
        if chat[1] == "E":
            answer.append(id_dict[chat[0]] + '님이 들어왔습니다.')
        else:
            answer.append(id_dict[chat[0]] + '님이 나갔습니다.')
    return answer