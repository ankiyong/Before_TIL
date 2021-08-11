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