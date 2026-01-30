J, N = map(int, input().split())

box_size = []

for _ in range(N):
	r, c = map(int, input().split())
	box_size.append(r*c)

box_size.sort(reverse=True)
cnt = 0

total_size = sum(box_size)
# print(total_size)

if total_size < J:
	cnt = -1
else:
	for i in range(N):
		J -= box_size[i]
		cnt += 1
		if J <= 0:
			break
print(cnt)