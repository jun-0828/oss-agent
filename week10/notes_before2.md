# week09/tools.py 함수 정리

`week09/tools.py`는 영화진흥위원회(KOBIS) 오픈 API의 **일별 박스오피스** 정보를 가져오는 도구 모음이다.

## 공통 사항

- `requests` 라이브러리로 API를 호출한다.
- API 키는 `secret.py`의 `API_KEY`에서 가져온다.
- 호출 주소(`BASE_URL`): `https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json`
- 요청 파라미터: `key`(API 키), `targetDt`(조회 날짜, `YYYYMMDD` 형식)
- 요청 타임아웃은 10초이고, HTTP 오류가 나면 `raise_for_status()`로 예외를 발생시킨다.
- 응답 JSON의 `boxOfficeResult` → `dailyBoxOfficeList`에서 영화 목록을 꺼내 사용한다.

## 함수 목록

### 1. `get_boxoffice_rank_1(date)`

- **역할:** 지정한 날짜의 박스오피스 1위 영화 제목을 반환한다.
- **매개변수:** `date` — 조회 날짜 (예: `"20251101"`)
- **반환값:** 1위 영화 제목 문자열 (`movieNm`)
- **동작:** 해당 날짜의 일별 박스오피스 목록을 받아 첫 번째 항목(`movies[0]`)의 제목을 돌려준다.

### 2. `get_movie_audience(date, title)`

- **역할:** 지정한 날짜에 특정 영화의 관객 수를 반환한다.
- **매개변수:**
  - `date` — 조회 날짜 (예: `"20251101"`)
  - `title` — 영화 제목 (박스오피스 목록의 제목과 정확히 일치해야 함)
- **반환값:**
  - 찾은 경우: 천 단위 쉼표가 들어간 관객 수 문자열 (예: `"123,456명"`)
  - 못 찾은 경우: `"'<제목>' 은(는) <날짜> 순위에 없습니다."`
- **동작:** 박스오피스 목록을 순회하며 제목이 일치하는 영화의 `audiCnt`(해당 일 관객 수)를 정수로 바꿔 형식화한다.

## 참고

- 두 함수 모두 API 호출과 응답 파싱 코드가 중복되어 있어, 공통 부분을 별도 함수로 분리할 수 있다.
- `get_boxoffice_rank_1`은 목록이 비어 있으면 `IndexError`가 발생할 수 있다.
