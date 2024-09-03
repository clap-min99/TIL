person = [15, 30, 50, 10]
n = len(person)
person.sort()  # [10, 15, 30, 50] 오름차순 정렬

total = 0
left_person = n - 1  # 화장실을 이용 아직 못한 대기자의 수

for turn in range(n):
    time = person[turn]
    total += left_person * time
    left_person -= 1

print(total)