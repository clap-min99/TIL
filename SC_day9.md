## GIT 사용법

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

        .code로 VSCode 실행
    
    3. 파일 확인 후 수정

        git add sth.txt         

    4. 변경 이력(commit) 남기기

        git commit -m 'changed!'

    5. git에 올리기
        
        git push origin master

    6. Git에서 변경된 내용 가져오기

        git pull origin master