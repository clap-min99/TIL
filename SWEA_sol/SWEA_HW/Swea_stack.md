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



