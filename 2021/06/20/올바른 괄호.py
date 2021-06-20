def solution(word):
    stack = 0
    for w in word:
        if w == "(":
            stack += 1
        elif w == ")":
            stack -= 1
        if stack < 0:
            return False
    else:
        if stack != 0:
            return False

    return True