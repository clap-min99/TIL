# 스타트캠프 8일차
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
### Git
버전을 관리하는 프로그램(분산 버전 관리 시스템)

#### 버전관리 

    변화를 기록하고 추적하는 것
    
    어디서 뭐가 변했는지 알 수 있고, 롤백도 가능

    마지막 파일과 이전 변경사항만 남기는 식

#### 중앙 vs 분산

- 중앙 집중식

        버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와서 다시 중앙에 업로드
    
- 분산식

        버전을 여러 개의 복제된 저장소에 저장 및 관리
        
        팀 작업 시 server computer(중앙서버)에 연결해서 버전을 확인 후 동기화

        (ex) 
        
        Server computer: ver3 , A : ver3 , B : ver3 

        A가 작업을 끝낸 후에 ver4를 만듦 → server computer ver 4

        B는 작업을 하기전에 중앙서버?를 확인. 동기화 후 ver 4로 만들고 작업 시작



- Git의 3가지 영역
    
    - **Working directory**
        
        실제 작업 중인 파일들이 위치하는 영역

    - **Staging area**

        working directory에서 변경된 파일 중, 다음 버전에 포함할 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

        임시저장 공간

        (ex) 100개 파일 중 3개 변경→ 변경한 3개만 저장하는 영역?

    - **Repository**

        버전(commit) 이력과 파일들이 **영구적으로 저장**되는 영역 
        모든 버전과 변경 이력이 기록됨
        
        * commit(버전)
            
            변경된  파일들을 저장하는 행위
            
            마치 사진을 찍듯이 기록한다 하며 snapshot이라고도 함

- Git 명령어
    - git init
        
        로컬 저장소 설정(초기화)

        git의 버전관리를 시작할 디렉토리에서 진행 

        git은 주로 CLI환경에서 사용

        - 주의사항
    
            git 로컬 저장소 내에 또다른 git 로컬 저장소를 만들지 말 것

            즉, 이미  git 로컬 저장소인 디렉토리 내부 하단에서 git init 명령어를 다시 입력하지 말 것

            git 저장소 안에 git 저장소가 있을 경우 가장 바깥쪽의  git 저장소가 안쪽의 git 저장소의 변경사항을 추적할 수 없기 때문

    - git add
        
        변경사항이 있는 파일을 staging area에 추가

        (ex)

        git add a.txt     

        git add layer2_1

        git add a.txt, layer2_1

        git add a.txt, b.txt = git add *.txt (.txt 형식을 다 올릴 것이다)

        git add . (지금 내가 관리하고 있는 파일을 전부 추가할 것이다)

    - git commit
    
        staging area 에 있는 파일들을 저장소에 기록

        해당 시점의 버전을 생성하고 변경 이력을 남기는 것 

        (ex)  git commit -m"login 기능 추가'

    - git commit --amend

        파일이나 커밋 메시지 형식을 잘못된 방법으로 지정했을 때 --amend 플래그를 이용해 실수를 해결할 수 있다.

        (ex) git commit --amend -m "an updated commit message"

    - git log

        commit history 보기

        -  git log --oneline

            commit 한 줄로 보기

        
    - git status



