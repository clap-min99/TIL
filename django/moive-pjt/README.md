# 06-pjt
남의 프로필 어떻게 가는데... 
내가 뭘할수있는데...


## 새로 알게 된 사실
브랜치 이동을 잘 하자...

현재 브랜치에서 하던 작업이랑 dev랑 충돌나면

현재 브랜치에서 `git stash`하면 임시 저장됨

`git pull origin dev` 하고 임시저장된 파일은 

`git stash drop`하면 버려진다


임시저장 목록 확인 <br>
`git stash list`

임시저장 작업 불러오기(가장 최근 stash가져옴)<br>
`git stash apply`
<br>


## git 프로젝트 flow 

### git flow

#### 팀장님
1. Repository 생성(readme 있는 상태로 만들기)
   
2. 같이 프로젝트 진행 할 팀원 초대
   
3. repository clone 받고 .gitignore 생성
   * .gitignore.io에서 만들기 python, django, venv, vue ...
4. django 프로젝트

   * 가상환경 설정(python -m venv venv)
   * django 설치
      
      `pip install django`
   
   * 설치한 library 저장(requirements.txt)

      `pip freeze > requirements.txt`

5. 개발자 모드로 전환(dev)
    * git branch dev, git switch dev(add, commit 하기 전)

6. git commit '환경 설정 전환'

7. django 시작
    
    ` django-admin startproject pjt .`

    `python manage.py startapp articles` -> settings.py에 등록

8. model class 생성

    * class Article(models.Model): ~~

    * 설계도 작성
  
      `python manage.py makemigrations`

    * db에 migrate
    
      `python manage.py migrate`

9.  추가로 설치
    
    `pip install django_extensions ipython` 
    
    -> settings.py에 django_extensions 등록

    -> requirements.txt에 저장(pip freeze > requirements.txt)


10. python shell ,, 
    
    `python manage.py shell_plus`
    

11. json 만들기

    `python manage.py dumpdata --indent=4 articles > articles.json`

    * fixture 폴더 만들기(json 저장용)

      `mkdir articles/fixtures` -> json 파일 fixtures로 옮기기 

12. add commit push

    같이 작업할 수 있도록 본인 repo로 가서 merge request 진행?

    근데 지금은 merge를 할 일이 없다.

    master는 일단 initial로 냅둘거다.(master에는 아무것도 없는 상태)


---
#### 팀원
1. `git branch dev`
2. `git switch dev`
3. `git pull origin dev`
  
    dev 에 있는 내용 받기
4. 가상환경 만들어서 `pip install -r requirements.txt`
5. `git branch accounts`
6. `git switch accounts`
7. `python manage.py startapp accounts`
   
    앱등록하기

    `AUTH_USER_MODEL = 'accounts.User'`
8. models.py

    `from django.contrib.auth.models import AbstractUser`

    `class User(AbstractUser):
        pass`

9. `makemigrations migrate`
10. `python manage.py createsuperuser`
11. `python manage.py dumpdata --indent=4 accounts > users.json`
12. `mkdir accounts/fixtures`
13. `mv users.json accounts/fixtures/`
14. `git add .`
 
    `git commit -m 'accounts'`

    `git push origin accounts`

15. merge request 만들기
16. accounts -> dev 로 가기<br>
    change branch 눌러서 master 로 되어 있던거 dev로 바꾸면 됨

---
#### 팀장님

1. settings branch 생성 후 바꾸기
   
   `git branch settings`
   
   `git switch settings`
   
2. settings에 base dir 바꿔주기
  
    `'DIRS': BASE_DIR/ 'templates'`

3. git add 후 base template 바꿨다고 commit 해주기
   
    `git add .`
  
    `git commit -m 'base template'`

4. settings 작업 후 commit 했고, 팀원도 다 했다고 연락옴?
   
    `git pull origin dev` 

    뭔가 많이 뜰 텐데 수정할 거 있으면 :wq 아니면 :q

5. git 상태 확인하고 settings push 하기
   
    `git status`

    `git push origin settings`

6. settings push 후 merge request 진행
  
    repository ㄱㄱ : 'settings -> dev' 로 merge 하기 

    (merge 후 settings branch에서 할 일이 다 끝나면 삭제된다.)

7. dev로 브랜치 바꾸고, 바꾼 내용(settings->dev) 받아오기
   
   `git switch dev`

   `git pull origin dev`

8. 이제 articles 작업할 articles branch 만들기

   `git branch articles`

   `git switch articles`

9. Article 관련 설정(1:N 관계 추가하기)

    ```py
    # articles/models.py
    class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      title = models.TextField()
    ```    

    model 변경 했으니 설게도 만들고 db로

    `python manage.py makemigrations`

    => user column 추가하려고 하면 default값 설정하라는 문구 같은게 나온다.
    user default 값은 integer가 되어야 하므로 1로 설정하자.

    `python manage.py migrate`

10. json 파일 만들기

  * user.json load하기
  
    `python manage.py loaddata user.json`

  * shell plus에서 user 만들기

    `python manage.py shell_plus`
    
    ```py
      # shell_plus

      user = User.objects.get(pk=1)

      article = Article()
      
      article.user = user

      article.title = 'test'

      article.save()

      exit()
    ```

    `python manage.py dumpdata --indent=4 articles > articles.json`

11. add commit push

    `git add`

    `git commit -m user article 1:N`

    `git push origin articles`
    
12. push 했으니까 merge request

    articles -> dev 로 ㄱㄱ 

--- 
팀원은 이제 내려받으면 된다. 

1. `git pull origin dev`


* merge block 당하면 resolve conflicts 누르지 말고 그 왼쪽에 있는 걸로 수정하기

---
프로필 페이지 수정하기 