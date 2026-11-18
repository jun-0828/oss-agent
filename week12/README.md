# boxoffice — KOBIS 박스오피스 조회 스킬

## 하는 일
- 날짜를 주고 "그날 박스오피스 1위가 뭐야?"라고 물으면 1위 영화 제목을 알려 줌
- 날짜와 영화 제목을 주고 관색 수를 물으면 그 영화의 일별 관객 수를 알려 줌
- 자료는 영화진흥위원회 KOBIS의 일별 박스오피스임

## 들어 있는 파일
- .claude/skills/boxoffice/SKILL.md
- .claude/skills/boxoffice/scripts/boxoffice.py
- .claude/skills/boxoffice/LICENSE

## 필요한 것
- Python 3
- requests 패키지 — `pip install requests` 로 설치함
- tools.py — 프로젝트 폴더
  - boxoffice.py 는 실행한 폴더에서 tools.py 를 찾아 그 안의 함수를 부름
- secret.py — tools.py 와 같은 폴더에 있어야 함. tools.py 가 여기서 `API_KEY` 를 읽어 감
- KOBIS 오픈 API(Open API, 공개 데이터 요청 창구) 키 — KOBIS 오픈 API 사이트에서 직접 발급받아야 함

## 설치
- 프로젝트 폴더에서 `pip install requests` 실행
- 프로젝트 폴더에서 Claude Code 를 실행
- "20261114 박스오피스 1위 영화를 알려줘"처럼 물어서 스킬이 쓰이는지 확인함
- 스크립트를 직접 돌려 볼 때는 프로젝트 폴더에서 아래처럼 실행함 (날짜는 8자리)

## 바깥으로 요청하는 곳
- `https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json`
  - KOBIS 일별 박스오피스 API(Application Programming Interface, 프로그램용 요청 창구)임

## 키
- 자기 키를 secret.py 에 넣을 것
- 이 저장소에는 키가 없음

## 권한
- SKILL.md 에 allowed-tools(허용 도구 목록) 항목이 없음
- SKILL.md 에 따라 Claude 는 tools.py, secret.py 를 읽거나 고치지 않고 스크립트만 실행함

## 라이선스
- MIT License
