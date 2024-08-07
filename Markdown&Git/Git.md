## 2024-07-12

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
    - **git config**

        git 최초 설정하기!
        
        사용자 이름, 이메일 주소 설정 -> git이 commit 할때마다 사용하는 정보

        사용자 이름 설정: git config --global user.name "NAME"

        사용자 이메일 설정: git config --global user.email "EMAIL"

        설정 확인하기: git config --list


    - **git init**
        
        로컬 저장소 설정(초기화)

        git의 버전관리를 시작할 디렉토리에서 진행 

        git은 주로 CLI환경에서 사용

        - 주의사항
    
            git 로컬 저장소 내에 또다른 git 로컬 저장소를 만들지 말 것

            즉, 이미  git 로컬 저장소인 디렉토리 내부 하단에서 git init 명령어를 다시 입력하지 말 것

            git 저장소 안에 git 저장소가 있을 경우 가장 바깥쪽의  git 저장소가 안쪽의 git 저장소의 변경사항을 추적할 수 없기 때문

    - **git add**
        
        변경사항이 있는 파일을 staging area에 추가

        (ex)

        git add a.txt     

        git add layer2_1

        git add a.txt, layer2_1

        git add a.txt, b.txt = git add *.txt (.txt 형식을 다 올릴 것이다)

        git add . (지금 내가 관리하고 있는 파일을 전부 추가할 것이다)

    - **git commit**
    
        staging area 에 있는 파일들을 저장소에 기록

        해당 시점의 버전을 생성하고 변경 이력을 남기는 것 

        (ex)  git commit -m"login 기능 추가'

    - **git commit --amend**

        파일이나 커밋 메시지 형식을 잘못된 방법으로 지정했을 때 --amend 플래그를 이용해 실수를 해결할 수 있다.

        (ex) git commit --amend -m "an updated commit message"

    - **git log**

        commit history 보기

        -  git log --oneline

            commit 한 줄로 보기

        
    - **git status**

        현재 로컬 저장소의 파일 상태 보기

    - **git remote -v**
        
        현재 로컬 저장소에 등록된 원격 저장소 목록 보기

    - **git remote add origin remote_repo_url**

        로컬 저장소에 원격 저장소 추가

        origin 자리에 원하는 이름 써도 된다
        (클라우드에 있는 원격 저장소 이름을 origin이라고 하는 것은 개발자들 사이의 관행 같은 것)

    - **git remote rm 원격_저장소_이름**

        현재 로컬 저장소에 등록된 원격 저장소 삭제
        (저장소는 남아있고 연결이 끊어지는 것)

    - **git push <remote><branch>**

        git push origin master
        원격 저장소에 commit 목록을 업로드
        로컬 저장소의 변경사항을 전송
        
    - **git pull <remote><branch>**
        
        git pull origin master
        로컬 저장소의 변경사항만을 받아옴
    
    - **git clone remote_repo_url**

        원격 저장소 전체를 복제(다운로드)
        (clone으로 받은 프로젝트는 git init 되어있음)
    
    - **git ignore**
        
        git에서 특정 파일이나 디렉토리를 추적하지 않도록 사용되는 텍스트 파일
        (프로젝트에 따라 공유하지 않아야 하는 것도 존재하기 때문)

        - 예시
            1. .gitignore 파일 생성

                파일명 앞에 '.' 입력, 확장자 없음
            
            2. a.txt와 b.txt 파일 생성

            3. gitignore에 a.txt 작성

            4. git init

            5. git status
        
        - gitignore 목록 생성 서비스

            [gitignore](https://www.toptal.com/developers/gitignore/)

#### 원격저장소란? (remote repository)
 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간


> GITHUB에 올리기

    1. 바탕화면에 파일 생성

        mkdir 파일명
    
    2. 파일 안에 텍스트 파일 생성
    
        touch sth.txt
    
    3. 텍스트 파일에 내용 작성(변경) 후 저장(ctrl+s)

    4. 파일을 Staging area에 놓기

        git add sth.txt
    
    5. 변경 이력 남기기

        git commit -m 'sth is changed'

    6. git 저장소(repositiory)와 연결하기

        git remote add origin <code>
        (origin은 지정가능, code는 repository 주소)

    7. git에 파일 올리기

        git push origin master
        (지정한 origin으로)

    8. git에 올라온 파일 가져오기

        git pull origin master 


> GITHUB에서 가져오기

    1. 바탕화면에 Git repository에 있는 파일 가져오기

        git clone <code>
        (.git 폴더가 생성되어 있으므로 git init 하지 않도록 주의!) 

    2. 파일에서 code 열기
    (파일은 Git 저장소명으로 저장됨)

        code. 으로 VSCode 실행
    
    3. 파일 확인 후 수정

        git add sth.txt         

    4. 변경 이력(commit) 남기기

        git commit -m 'changed!'

    5. git에 올리기
        
        git push origin master

    6. Git에서 변경된 내용 가져오기

        git pull origin master


> 







#### GitHuB 활용하기
- TIL을 통해 내가 학습하는 것을 기록
    - TIL(Today I learned)
        매일 내가 배운 것을 마크다운으로 정리해서 문서화 하는 것

- 개인, 팀 프로젝트 코드를 공유
    개발 면접 지원 시 본인의 GitHub 주소를 공유해 어떤 프로젝트를 진행했고,
    어떤 코드를 작성했는지 공유하고 평가받기 위해 사용

- 오픈 소스 프로젝트에 기여

- README.md 파일
    
    프로젝트에 대한 설명, 사용방법, 문서화된 정보 등을 포함하는 역할

    markdown 형식으로 작성