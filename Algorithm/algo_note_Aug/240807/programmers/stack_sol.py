import math


def solution(progresses, speeds):
    spend_date = []
    for i in range(len(progresses)):
        done = (100 - progresses[i]) / speeds[i]
        spend_date.append(math.ceil(done))

    cnt = 1
    answer = []
    for j in range(len(spend_date)-1):      # spend_date
        for k in range(len(spend_date)-j-1):
            if spend_date[j] >= spend_date[j+k]:
                cnt += 1

            else:
                answer.append(cnt)
                cnt = 0
                j += cnt







    # answer = []
    #
    # return answer






#debugging
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# spend_date = []
# for i in range(len(progresses)):
#     done = (100 - progresses[i]) / speeds[i]
#     spend_date.append(math.ceil(done))
# print(spend_date)