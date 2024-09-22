

arr = [input() for _ in range(5)]

for i in range(15):                     # 단어 길이 최대 15
    for j in range(len(arr)):
        if i >= len(arr[j]):            # 읽으려는 최대 글자 수 넘으면
            continue                    # 넘기고 다시 for 문 반복
        print((arr[j][i]), end='')

