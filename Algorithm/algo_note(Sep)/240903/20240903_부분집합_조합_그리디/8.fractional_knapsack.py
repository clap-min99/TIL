n = 3
target = 30  # Knapsack KG
things = [(5, 50), (10, 60), (20, 140)]  # (Kg, Price)

# (Price / Kg) 기준으로 내림차순 sort
things.sort(key=lambda x: (x[1] / x[0]), reverse=True)
# sort 결과 = [(5, 50), (20, 140), (10, 60)]
print(things)

total = 0
for kg, price in things:
    per_price = price / kg

    # 만약 가방에 남은 용량이 얼마되지 않는다면,
    # 물건을 잘라 가방에 넣고 끝낸다.
    if target < kg:
        total += target * per_price
        break

    total += price
    target -= kg

print(int(total))
