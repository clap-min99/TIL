### stack

#### 괄호 검사
* 괄호의 짝을 검사하는 프로그램을 작성해 봅시다.
* 작성한 프로그램으로 다음 괄호 사용을 검사해 봅시다.
 

[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[예제 입력]

4
()()((()))

((()((((()()((()())((())))))

(())(((())()))(()()((()))

))))

[예제 출력]

 #1 1

 #2 -1

 #3 -1

 #4 -1

```py
def bracket_inspect(bracket):
    stack = []
    for char in bracket:
        if char == '(':             # 열린 괄호 만나면
            stack.append(char)      # stack에 넣기
        elif char == ')':           # 닫힌 괄호 만났을 때
            # stack에 아무것도 없거나 스택의 마지막 요소(가장 최근 요소)가 열린괄호가 아니면
            if not stack or stack[-1] != '(':
                return -1           # -1 반환
            stack.pop()             # 짝이 맞으면 pop해서 없애줌
    if len(stack) == 0:             # 문자열 모두 순회했을 때 stack이 0이면
        return 1                    # 모두 짝을 맞춰서 나갔다는 뜻이므로 1 반환

    return -1                       # 그렇지 않으면(stack에 요소 남으면) -1 반환


T = int(input())
for tc in range(1, T+1):
    bracket_matching = input()
    a = bracket_inspect(bracket_matching)
    print(f'#{tc} {a}')
```
---
#### 반복문자 지우기
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
 

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
 

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.

CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.

CAA 연속 문자 AA를 지운다.

C 1글자가 남았으므로 1을 리턴한다.


[입력]
 
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
 

다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.

 

[출력]
 
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.


```py
# 단어 순회하면서 검사하고, 겹치면 삭제
T = int(input())

for tc in range(1, T+1):
    word = input()
    N = len(word)
    word_list = []
    for i in range(N):
        word_list.append(word[i])           # word를 list로 만듦
    x = 0                                   # x는 단어의 index를 의미
    while x < len(word_list)-1:             # 앞, 뒤 단어를 모두 검사하므로 (전체길이-1)까지 검사
        if word_list[x] == word_list[x+1]: 
            del word_list[x:x+2]            # 두 단어가 같다면 x, x+1 지우기
            x = 0                           # 다시 처음부터 검사해야 하므로 x 초기화
        elif word_list[x] != word_list[x+1]:  # 두 단어가 다르면 
            x += 1                            # 인덱스 +1해서 계속 검사
            continue
    ans = len(word_list)

    print(f'#{tc} {ans}')
```
```py
# stack 이용해서 풀기 
T = int(input())

for tc in range(1, T+1):
    stack = []
    word = input()
    for idx in word:
        if not stack or idx != stack[-1]:
            # stack에 아무것도 없거나, 비교할 글자가 가장 최근에 append한 글자와 다를 때
            stack.append(idx)     # stack에 단어 쌓기
        elif idx == stack[-1]:    # 비교할 글자가 가장 최근에 append한 글자와 같으면
            stack.pop()           # stack의 top에 있는 글자 빼기

    ans = len(stack)
    print(f'#{tc} {ans}')
```
- Sol point
    연속된 글자끼리 비교하면서 쌓아가기 
    stack에 쌓아가면서 가장 최근에 append한 글자를 하나씩 비교하여
    같다면 pop(가장 최근에 append한 글자를 뽑아냄) 아니면 stack에 쌓아가는 방식
    
    stack에 처음 단어를 넣을 때 stack에 아무것도 없을 때도 고려해야함,,
    (if not stack)
---
#### 괄호 검사 2

주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
 

예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
 

정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
 

print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.


 

[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

```py
def check_match(expression):
    bracket_dict = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in expression:                     # 문자열의 각 문자를 순회
        if char in bracket_dict.values():       # 열린괄호 만나면
            stack.append(char)                  # stack에 넣기
        elif char in bracket_dict.keys():       # 닫힌괄호 만나면
            if not stack or stack[-1] != bracket_dict[char]:
                return 0
            stack.pop()
    if len(stack) == 0:
        return 1

    return 0


T = int(input())
for tc in range(1, T+1):
    bracket_word = input()
    ans = check_match(bracket_word)
    print(f'#{tc} {ans}')

```
Sol_point
1. 닫힌 괄호는 가장 최근에 나온 열린 괄호와 짝이다.
2. 열린괄호를 stack에 먼저 넣고, 열린괄호와 닫힌 괄호와의 짝이 맞으면 pop
3. 마지막 stack에 요소가 없으면 모두 짝이 맞는 것.
---

#### 기능개발(ㅍㄹㄱㄹㅁㅅ)
문제 설명

프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.


|progresses | speeds | return|
|------|------|------|   
|[93, 30, 55] |	[1, 30, 5] | [2, 1] |
|[95, 90, 99, 99, 80, 99] |	[1, 1, 1, 1, 1, 1] |[1, 3, 2] |

```py
import math

def solution(progresses, speeds):
    spend_date = []
    for i in range(len(progresses)):
        done = (100 - progresses[i]) / speeds[i]
        spend_date.append(math.ceil(done))  # 소요되는 날짜를 리스트에 저장

    cur = 0                     # 현재 인덱스(기준 인덱스)
    comp = 1                    # 더해가면서 비교할 인덱스
    cnt = 1                     # 한번에 배포도는 개수 count
    result = []

    # 현재 기준이 되는 인덱스(cur)에 있는 작업 날짜보다
    # 더 많은 날짜가 소요되는 날 직전까지의 작업 개수를 더해 result에 count해서 저장

    while cur < len(spend_date):                # 현재 인덱스가 리스트의 개수와 같아질 때까지
        if cur + comp == len(spend_date):   # 마지막 인덱스까지 비교 끝났으면
            result.append(cnt)                  # cnt 결과에 저장
            return result

        if spend_date[cur] >= spend_date[cur + comp]:  # 현재 인덱스가 다음 인덱스보다 크면
            cnt += 1  # count +1
            comp += 1  # 비교 인덱스 +1
            continue

        if spend_date[cur] < spend_date[cur + comp]:  # 현재 인덱스가 다음 인덱스보다 작으면
            result.append(cnt)  # 결과값에 count한 개수를 저장하고
            cur += cnt      # 현재 인덱스에 cnt만큼 더하기
            cnt = 1         # cnt는 1로 초기화
            comp = 1        # 비교 인덱스도 1로 초기화


print(solution([93, 30, 55],[1, 30, 5]))
```
Sol point
- 현재 인덱스와 비교 인덱스를 따로 설정
- 파이참 디버깅 적극활용하기! 
---
#### 파스칼 삼각형(#2005)
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N이 4일 경우,
 
1

1   1

1   2   1

1   3   3   1


N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.


[제약 사항]

파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.

삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```py
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
 
    # 첫번째 행은 항상 [1]
    prev_stack = [1]
    print(1)
 
    # 파스칼 삼각형은 1로 시작해서 1로 끝나고, 그 사이값은 이전 행의 두 값의 합으로 구성된다.
    # 첫 번째 줄은 이미 [1]로 셋팅을 했으므로, 2번째 줄부터 진행
    for i in range(1, N):
        new_stack = [1]
 
        for j in range(len(prev_stack)-1):
            new_stack.append(prev_stack[j] + prev_stack[j+1])
 
        new_stack.append(1)
 
        print(' '.join(map(str, new_stack)))
 
        prev_stack = new_stack
```
---