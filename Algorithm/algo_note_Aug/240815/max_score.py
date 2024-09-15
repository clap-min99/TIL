# 최대 성적표 만들기

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    score = sorted(map(int, input().split()))   
    max_s = []
    for i in range(K):
        max_s.append(score.pop())
    print(f'#{tc} {sum(max_s)}')

