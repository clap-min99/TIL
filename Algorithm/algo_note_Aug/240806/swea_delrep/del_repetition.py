T = int(input())

for tc in range(1, T+1):
    word = input()
    N = len(word)
    word_list = []
    for i in range(N):
        word_list.append(word[i])           # word를 list로 만듦
    x = 0                                   # x는 단어의 index를 의미
    while x < len(word_list)-1:             # 앞, 뒤 단어를 모두 검사하므로 (전체길이-1)까지 검사
        if word_list[x] == word_list[x+1]:
            del word_list[x:x+2]            # 두 단어가 같다면 x, x+1 지우기
            x = 0                           # 다시 처음부터 검사해야 하므로 x 초기화
        elif word_list[x] != word_list[x+1]:  # 두 단어가 다르면
            x += 1                            # 인덱스 +1해서 계속 검사
            continue
    ans = len(word_list)

    print(f'#{tc} {ans}')



