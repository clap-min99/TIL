'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

T = int(input()) # 테스트케이스 개수

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for i in range(N):
        if max_v < arr[i]:
            max_v = arr[i]
    for j in range(N):
        if min_v > arr[j]:
            min_v = arr[j]
    answer = int(max_v) - int(min_v)
    print(f'#{tc} {answer}')
