### CLASS2_SOL

#### 직각삼각형(#4153)
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

**입력**

입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

**출력**

각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

```py
while True:
  length = list(map(int, input().split()))
  
  if length[0] ==0 and length[1] ==0 and length[2] == 0:
    break

  length.sort()
  a, b, c = length

  if a**2 + b**2 == c**2:
    print('right')
  else:
    print('wrong')
```
* sol point
  
  length list를 sort해서 가장 긴 값을 지정하기!


---
#### 단어정렬(#1181)

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

**입력**

첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

**출력**

조건에 따라 정렬하여 단어들을 출력한다.

```py
word_cnt = int(input())
word_list = []
for i in range(word_cnt):
  a = input()
  word_list.append(a)

rm_dup = set(word_list)    # list를 set으로 바꿔 중복 제거
ans = list(rm_dup)         # set을 다시 list로

ans.sort()                 # 문자열을 사전 순서로 정렬
ans.sort(key=len)          # 문자열의 길이 기준으로 정렬 

for i in range(len(ans)):
  print(ans[i])
```
* sol point

  list a를 정렬하는 방법
    - a.sort()

      : 사전식 순서로 정렬
  
    - a.sort(key=len)

      : 문자열 길이를 기준으로 정렬

---