def check_match(expression):
    bracket_dict = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in expression:                     # 문자열의 각 문자를 순회
        if char in bracket_dict.values():       # 열린괄호 만나면
            stack.append(char)                  # stack에 넣기
        elif char in bracket_dict.keys():       # 닫힌괄호 만나면
            if not stack or stack[-1] != bracket_dict[char]:
                return 0
            stack.pop()
    if len(stack) == 0:
        return 1

    return 0


T = int(input())
for tc in range(1, T+1):
    bracket_word = input()
    ans = check_match(bracket_word)
    print(f'#{tc} {ans}')






