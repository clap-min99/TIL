import time


# 매번 출력하는 경우
start_time = time.time()
for i in range(50000):
    print(i)
end_time = time.time()
print(f"{end_time - start_time:.4f}")

# 결과 저장 후 한 번에 출력하는 경우
start_time = time.time()
results = []
for i in range(50000):
    results.append(i)
print(results)
end_time = time.time()
print(f"{end_time - start_time:.4f}")
