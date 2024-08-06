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
