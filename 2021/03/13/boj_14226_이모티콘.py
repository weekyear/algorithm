import sys
sys.stdin = open('input_14226.txt', 'r')

S = int(input())

result = 0
Q = [(1, 0, 0)]
visited = {}

while True:
    num_emoticon, clipboard, time = Q.pop(0)

    # 화면에 있는 이모티콘 수와 클립보드에 저장되어 있는 이모티콘 수가 동일한 경우
    # 불필요한 계산을 하게 되면 시간초과가 뜨므로 걸러준다.
    if visited.get((num_emoticon, clipboard)) is None:
        visited[(num_emoticon, clipboard)] = 1
        # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        if num_emoticon != clipboard:
            Q.append((num_emoticon, num_emoticon, time + 1))

        # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        if clipboard > 0:
            added_num_emoticon = num_emoticon + clipboard
            if added_num_emoticon == S:
                result = time + 1
                break
            Q.append((added_num_emoticon, clipboard, time + 1))

        # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
        if num_emoticon > 1:
            if num_emoticon - 1 == S:
                result = time + 1
                break
            Q.append((num_emoticon - 1, clipboard, time + 1))

print(result)