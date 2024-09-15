# 2292 벌집

def sigma(n):
  a = 1
  for i in range(n):
    s = 6*i
    a += s
  return a

def bee(N, x):
  comp = sigma(x)
  comp2 = sigma(x+1)
  if comp < N <= comp2:
    print(x+1)
  else:
    bee(N, x+1)

N = int(input())
bee(N, 1)