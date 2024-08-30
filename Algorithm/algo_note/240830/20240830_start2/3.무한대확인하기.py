value = 1.8
count = 0

while value < float('inf'):
    value *= 10
    count += 1

print(f"10을 {count}번 곱하면 값이 무한대(inf)와 같습니다.")

value = 5.0
count = 0

while value > float('-inf'):
    value *= -10
    count += 1

print(f"-10을 {count}번 곱하면 값이 음의 무한대(-inf)와 같습니다.")