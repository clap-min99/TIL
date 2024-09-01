# Programmers 기능개발

import math


def solution(progresses, speeds):
    spend_date = []
    for i in range(len(progresses)):
        done = (100 - progresses[i]) / speeds[i]
        spend_date.append(math.ceil(done))  # 소요되는 날짜를 리스트에 저장

    cur = 0                     # 현재 인덱스(기준 인덱스)
    comp = 1                    # 더해가면서 비교할 인덱스
    cnt = 1                     # 한번에 배포도는 개수 count
    result = []

    # 현재 기준이 되는 인덱스(cur)에 있는 작업 날짜보다
    # 더 많은 날짜가 소요되는 날 직전까지의 작업 개수를 더해 result에 count해서 저장

    while cur < len(spend_date):                # 현재 인덱스가 리스트의 개수와 같아질 때까지
        if cur + comp == len(spend_date):   # 마지막 인덱스까지 비교 끝났으면
            result.append(cnt)                  # cnt 결과에 저장
            return result

        if spend_date[cur] >= spend_date[cur + comp]:  # 현재 인덱스가 다음 인덱스보다 크면
            cnt += 1  # count +1
            comp += 1  # 비교 인덱스 +1
            continue

        if spend_date[cur] < spend_date[cur + comp]:  # 현재 인덱스가 다음 인덱스보다 작으면
            result.append(cnt)  # 결과값에 count한 개수를 저장하고
            cur += cnt      # 현재 인덱스에 cnt만큼 더하기
            cnt = 1         # cnt는 1로 초기화
            comp = 1        # 비교 인덱스도 1로 초기화


print(solution([93, 30, 55], [1, 30, 5]))