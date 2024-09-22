### String

#### String

주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.

Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.

위 문장에서 ti 를 검색하면, 답은 4이다.

[제약 사항]

총 10개의 테스트 케이스가 주어진다.

문장의 길이는 1000자를 넘어가지 않는다.

한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.

한 문장에서는 하나의 문자열만 검색한다.

[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.

[출력]

부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

[예제 입력]

1

ti

Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasics ...


2

ing

Thedoublehelixformsthestructuralbasisofsemi-conservativeDNAreplication.1,2Less ...

[예제 출력]

- #1 4
- #2 2

```py
Testcase = 10

for _ in range(1, Testcase+1):
  tc = int(input())
  pattern = input()
  search_txt = input()
  result = 0

  pattern_idx = 0        # 비교할 부분을 가리키는 패턴의 인덱스
  compare_idx = 0        # 비교할 부분을 가리키는 문자열 인덱스

  while compare_idx < len(search_txt):
    if search_txt[compare_idx] != pattern[pattern_idx]:
      compare_idx = compare_idx - pattern_idx + 1
      pattern_idx = 0
      continue


    pattern_idx += 1
    compare_idx += 1

    if pattern_idx == len(pattern):
      result += 1
      pattern_idx = 0
      compare_idx = compare_idx - pattern_idx + 1

  print(f'#{tc} {result}')
```
---
