
가상환경 구축
  * pip install virtualenv
  * 프로젝트 루트에서 python3 -m venv venv


가상환경 적용
* source venv/bin/activate


패키지 설치
* 프로젝트 루트에서 pip install -r requirements.txt


패키지 설치 후 목록 업데이트
* 프로젝트 루트에서 pip freeze > requirements.txt


테스트서버 실행
* 프로젝트 루트에서 python manage.py runserver

