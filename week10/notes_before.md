# week09/tools.py 함수 정리

`week09/tools.py`는 영화진흥위원회(KOBIS) 오픈 API의 **일별 박스오피스** 엔드포인트를 호출해 정보를 가져오는 도구 모음이다.

## 공통 사항

- API 키는 `secret.py`의 `API_KEY`에서 가져온다.
- 요청 주소(`BASE_URL`):
  `https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json`
- 두 함수 모두 `requests.get`으로 요청하며 `timeout=10`을 사용하고, HTTP 오류가 나면 `raise_for_status()`로 예외를 발생시킨다.
- 응답 JSON의 `boxOfficeResult.dailyBoxOfficeList`에서 영화 목록을 꺼내 사용한다.
- `date`는 `YYYYMMDD` 형식의 문자열이다 (예: `"20251101"`).

## 함수 목록

### `get_boxoffice_rank_1(date)`

- **역할:** 지정한 날짜의 박스오피스 1위 영화 제목을 반환한다.
- **매개변수:** `date` — 조회할 날짜 (`YYYYMMDD`)
- **반환값:** 1위 영화 제목 문자열 (`movieNm`)
- **동작:** 일별 박스오피스 목록의 첫 번째 항목(`movies[0]`)의 제목을 돌려준다.

### `get_movie_audience(date, title)`

- **역할:** 지정한 날짜에 특정 영화의 관객 수를 반환한다.
- **매개변수:**
  - `date` — 조회할 날짜 (`YYYYMMDD`)
  - `title` — 영화 제목 (박스오피스 목록의 제목과 정확히 일치해야 함)
- **반환값:**
  - 영화를 찾으면 천 단위 쉼표가 들어간 관객 수 문자열 (예: `"123,456명"`)
  - 찾지 못하면 `"'<title>' 은(는) <date> 순위에 없습니다."` 메시지
- **동작:** 목록을 순회하며 `movieNm`이 `title`과 같은 영화의 `audiCnt`(해당 일 관객 수)를 정수로 바꿔 포맷한다.

## 참고 / 개선할 점

- 두 함수에 API 호출 및 목록 추출 코드가 중복되어 있다 → 공통 함수로 분리할 수 있다.
- `get_boxoffice_rank_1`은 목록이 비어 있으면 `IndexError`가 발생한다.
- `get_movie_audience`는 결과를 찾지 못한 경우에도 오류 대신 문자열을 반환하므로, 호출하는 쪽에서 성공/실패를 구분하기 어렵다.
