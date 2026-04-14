# 1. 가상환경: 개발자는 기본적으로 가상환경은 필수적으로 구축을 해야한다.

# 1. 가상환경은 라이브러리 충돌을 방지시켜줄 수 있다.
# Global(전역) 설치를 할 시 위험성: 파이썬을 처음 설치하면 컴퓨터 전체에 영향을 미치는 공간에 패키지가 깔린다.
# 1년뒤 다른 프로젝트를 하다가 패키지 버젼을 업데이트하면 예전에 만들어준 프로젝트가 작동하지 않는다.

# 격리(Isolation) : 프로젝트마다 담장을 쌓는 것이다.

# cmd 명령어(Linux명령어와 많은 부분들이 유사함)
# 1. cd : changeDirectory : 폴더를 변경
# 2. mkdir : makedirectory : 폴더를 생성
# 3. python -m venv .venv : 프로젝트 전용 파이썬 복사본

# 4. 가상환경 활성화 : .venv\Scripts\activate
# 경로를 확실히 잘 잡아줘야 한다.


# <<Windows PowerShell>>

# 설치하기: 격리된방(가상환경)에서 필요한 도구들을 들여놓기
# 크롤링을 하기위해서는 2가지 모듈이 대체적으로 사용되는데 requests와 beautifulsoup2가 존재.
# requests 설치: pip install requests
# 기록하기(협업준비) : 내가 무엇을 설치했는지. 메모장파일로 저장.
# pip freeze > requirements.txt

# FastAPI 와 Uvicorn 설치

# FastAPI : 파이썬으로 API(데이터를 주고받는 통로)를 만들기 위한 프레임워크

# Uvicorn : 웹서버 : FastAPi로 만든 코드를 실제로 실행시켜서 웹에 띄워주는 웹서버다.

# 1. 도구들 설치
# pip install fastapi uvicorn

# 2. 웹 서버 실행 코드 : uvicorn main:app --reload


# 3. Swagger UI : 내가 짠 코드를 기반으로 자동으로 API 설명서가 만들어집니다.
# 방법 : 브라우저 주소 뒤에 /docs만 붙이면 가능
# http://127.0.0.1:8000/docs

# 설명 : 내가 짠 코드를 기반으로 자동으로 APi 설명서가 만들어진다.
# Try it out 버튼으로 직접 API테스트 가능


# 크롤링을 하기위해서는 1. Requests가 필요하고 2번째로는 BeautifulSoup가 필요하다.

# Requests : 브라우저 대신 특정 웹사이트에서 데이터를 주세요 라는 요청을 보내는 도구
# Beautifulsoup : 가져온 복잡한 Html 코드 뭉치에서 원하는 "제목"이나 "가격"만 골라오는 집게 역할을 한다.

