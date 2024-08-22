from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
card = []
for i in range(1, N+1):
    card.append(i)

q = deque(card)
discard = []

while q:
    if len(q) == 1:
        break
    discard.append(q.popleft())
    q.rotate(-1)

print(*discard, q[0])
