1. 가상환경 생성 

2. 2.django 인스톨

3. django  프로젝트 시작

   - django-admin startproject ToDoList

4. django app 시작(필요한만큼 생성)

   - python manage.py startapp my_to_do_app

   4.1 생성된 app는 프로젝트에 등록 해줘야 함

- 생성된 파이참 프로젝트 이름 : ToDoList

- 생성된 django프로젝트 이름 : ToDoList > settings.py에 

  생성된 app 등록해야함

  setting.py파일열고 INSTALLED_APPS = [] 에 앱 이름 등록

- 생성된 app 이름 : my_to_do_list

5. django migrate 진행

   - 데이터베이스에 테이블, 필드 등의 변경이 발생했을 때 지정된 

     데이터 베이스에 적용하는 과정을 의미

     - 프로젝트 생성 후 기본 마이그레이션 진행
     - python manage.py migrate

6. 서버 구동 코드
   - python manage.py renserver

7. 연결주소
   - http://127.0.0.1:8000
   - http://localhost:8000
     -  -> 현재 개발중인 컴퓨터에서 프로그램 번호가 8000번(장고) 인 프로그램으로 요청을 보낼

#### 프로젝트 개발

1. http://127.0.0.1:8000 으로 클라이언트가 요청하면 브라우저에 index 라는 문구를 출력

   1. url 구성  : 기능별로 구성 파일을 분리해서 개발

      - ToDoList.urls.py 파일에서 진행

      - paht(' ',include('my_to_do_app.urls')),

        => ' ' : http://128.0.1:8000 

        ​	include('my_to_do_app.urls') : 요청에 의항 처리 함수는 my_to_do_app.urls.py 에 가서 한번 더 확인할 것

      - 새로 my_to_do_app.urls 파일 생성

        ```python
        # my_to_do_app > urls.py
        from django.urls import path
        from . import views
        urlpatterns = [
            path('',views.index,name='index'),
            #root url conf에 의해서 http://127.0.0.1:8000의 요청이 전달되면
            #views.py 파일의 index 수 코드를 실행
            #http://127.0.0.1:8000 url의 별명은 index
            ]
        ```

   2.  요청시 처리할 코드 생성

      - my_to_do_app.views.py 파일에서 진행

      - my_to_do_app.views.py에 index 함수 생성

        ```python
        def index(request): #요청에 의해 처리되는 함수는 파라미터가 전달 되던 안되던 무조건 request를 인수로 설정해야 한다
            return HttpResponse('my_to_do_app first page')
            # 요청에 대한 응답 객체를 생성해서 바로 클라이언트로 반환
        ```

   3. 템플릿(front_end 파일 연결)

      - 클라이언트 요청시 전송될 파일 저장(저장 폴더 결정)

      - setting.py에 의해 템플릿은 

        ```
        my_to_do_app > Templates > my_to_do_app > *.html/*.css/*.js
        ```

      - my_to_do_app > views.py 파일에서

        html 파일을 rendering 하도록 코드를 수정

        -> 구성된 html 파일을 반환되도록 하는 작업

        - return render(request객체,반환해줄 html 경로와 파일명)

          ```python
          def index(request): #요청에 의해 처리되는 함수는 파라미터가 전달 되던 안되던 무조건 request를 인수로 설정해야 한다
              return render(request,'my_to_do_app/index.html')#Templates/my_to_do_app/index.html
          ```

        

      

      4. 메모하기 버튼 동작코드 생성

         기능 : 사용자가 입력한 data를 db에 저장

      -  html form 태그의 action 속성 지정(url 구성)

        => <form action="./createTodo/"https://127.0.0.1:8000/createTodo/

        

        - views.py에서 처리 코드 생성

        - ```python
          def createTodo(request):
              #사용자가 메모에 입력해서 넘긴 값을 반환하는 코드
              # return HttpResponse('createTodo 메모 작성') # 요청에 응답하는지만 확인
          ```

        #사용자가 메모에 입력해서 넘긴 값을 반환하는 코드 

        html 파일에서 어떤 name으로 값이 전달되는지 확인 :

        todoCintetn변수에 입력된 data가 담겨서 서버로 전달

        

```python
<input id="todoContent" name="todoContent"
```

method = 'POST'로 설정되어 있음

```python
def createTodo(request):

    user_input_str = request.POST['todoContent']
    return HttpResponse("입력한 메모 데이터 : "+user_input_str)
```

사용자가 입력해서 넘긴 값을 db에 저장



- DB관련 코딩

  models.py – 테이블 정의 (class로 생성 models.Model을 상속받아서 생성)
  admins.py – 정의된 테이블이 admin 화면에 보이게 함
  manage.py makemigrations – 데이터베이스에 변경이 필요한 사항을 추출
  manage.py migrate – 데이터베이스에 변경사항을 반영
  manage.py runserver – 현재까지 작업 개발을 웹서버로 확인

  1. 모델 생성

     ```python
     from django.db import models
     # Create your models here.
     
     class Todo(models.Model): #models.Model 을 상속받아 Django 모델 class 생성
         #컬럼 지정
         content = models.CharField(max_length=255) # 교재 175쪽 참고
     ```

  2. 모델의 변경사항 추출

     python manage.py makemigrations

  3.  변경된 모델 사항 DB에 반영

     python manage.py makemigrations

  4.  dbshell 이용해서 변경사항 db에 반영되었는지 확인

     python manage.py dbshell

     .tables

     PRAGMA table_info(my_.to_do_app_todo)

