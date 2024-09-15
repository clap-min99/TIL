import time


# 매번 출력하는 경우
start_time = time.time()
for i in range(50000):
    print(i)
end_time = time.time()
print(f"매번 출력하는 시간: {end_time - start_time:.4f}초")

# 결과 저장 후 한 번에 출력하는 경우
start_time = time.time()
results = []
for i in range(50000):
    results.append(i)
print(results)
end_time = time.time()
print(f"결과 저장 후 출력하는 시간: {end_time - start_time:.4f}초")
