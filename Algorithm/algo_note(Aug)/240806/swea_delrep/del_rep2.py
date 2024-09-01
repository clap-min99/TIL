T = int(input())

for tc in range(1, T+1):
    stack = []
    word = input()
    for idx in word:
        if not stack or idx != stack[-1]:
            # stack에 아무것도 없거나, 비교할 글자가 가장 최근에 append한 글자와 다를 때
            stack.append(idx)     # stack에 단어 쌓기
        elif idx == stack[-1]:    # 비교할 글자가 가장 최근에 append한 글자와 같으면
            stack.pop()           # stack의 top에 있는 글자 빼기

    ans = len(stack)
    print(f'#{tc} {ans}')