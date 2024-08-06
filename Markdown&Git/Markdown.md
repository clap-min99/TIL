## 2024-07-11

### 마크다운(Markdown)
-  마크다운을 사용하는 이유
    - 개발자들끼리 코드를 서로 주고받기 좋음
    - 글을 쓰면서 서식을 설정할 수 있음
    - 문법이 간단한 편이다
    - 개발자들의 소통방식 (git hub)

- 마크다운 사용법
    - #: heading1
    - ##: heading2
    - -: list
    - ** **: bold
    - *{} *: Italic
    - ---: horizontal rule
    - '>': blockquote
    -  [이름](url): link  
    - ![alt](url): image
    - Table
        |헤더1|헤더2|헤더3|
        |------|------|------|
        |내용1|내용2|내용3|
        |내용4|내용5|내용6|
    - 소스코드
        ```python
        print (f"나는 어제 {%d}시에 잠들었어", %d)
        ```
---    
### GUI와 CLI
- GUI 
    
    그래픽을 통해 사용자와 컴퓨터가 상호작용하는 방식

- CLI
    - directory?
        - 위계구조를 나누는 방법
        - 지금은 폴더의 개념으로 생각해도 무관

    - **경로**(현재 나의 위치)를 아는 것이 중요

    - 기초문법
        - dash
            
            dash 명령어에서는 스페이스를 사용하면 단어를 따로 인식한다.
           
           파일명을 영어로 하고 스페이스는 사용하지 않는다. 
           
           단어 사이에 공백을 나타내고 싶으면 언더바(_)를 사용한다.
        - ls

            현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 출력
                (ls-a 는 숨김파일까지 보는것.(a는 all을 의미))

        - cd(change directory)

            cd. : 현재 디렉토리

            cd.. : 현재의 상위 디렉토리

            cd 파일명 : 하위 디렉토리로 이동

            cd 파일명1/파일명2 
            
            : 파일명 1에 있는 파일명2로 이동. 하위 파일로 계속 이동하려면 슬래시(/)사용
            
            ex. 
            
            cd layer1/layer2
           
            cd ../..

        - mkdir

            새 디렉토리 생성
        
        - touch 

            파일 생성 

            (ex)touch a.txt 메모장 만들기

        - start

            파일 열기 

            (ex) start a.txt 메모장 열기
        
        - pwd(print working directory)

            어떤 OS를 사용하든지 사용 가능

            root directory부터 현재까지의 경로를 보여줌(절대경로)

            ex. /c/Users/SSAFY/Desktop/layer1

            * 상대경로
                
                현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것

                만약 현재 작업하고 있는 디렉토리가 C:/Users 일때 윈도우 바탕화면으로의 상대경로는 ssafy/Desktop

---