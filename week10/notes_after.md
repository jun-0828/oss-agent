작성 : Claude Code / 확인 : 이경준

# week09/tools.py 함수 정리

- 영화진흥위원회(KOBIS) 오픈 API의 일별 박스오피스 정보를 가져오는 도구 모음임

## 공통 사항

- API 키는 `secret.py`의 `API_KEY`를 가져와 씀
- 요청 주소(`BASE_URL`)는 `https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json`임
- 두 함수 모두 `requests.get`으로 요청하고 `timeout=10`을 지정함
- HTTP 오류가 나면 `raise_for_status()`로 예외를 발생시킴
- 응답 JSON의 `boxOfficeResult` → `dailyBoxOfficeList`에서 영화 목록을 꺼내 씀
- `date`는 `YYYYMMDD` 형식 문자열임 (예: `"20251101"`)

## 함수 목록

### `get_boxoffice_rank_1(date)`

- 역할 : 지정한 날짜의 박스오피스 1위 영화 제목을 돌려줌
- 매개변수 : `date` (조회할 날짜)
- 반환값 : 1위 영화 제목 문자열 (`movieNm`)
- 동작 : 영화 목록의 첫 번째 항목(`movies[0]`)에서 제목을 꺼냄

### `get_movie_audience(date, title)`

- 역할 : 지정한 날짜에 특정 영화의 관객 수를 돌려줌
- 매개변수
  - `date` : 조회할 날짜
  - `title` : 영화 제목 (목록의 제목과 정확히 같아야 함)
- 반환값
  - 찾으면 천 단위 쉼표를 넣은 관객 수 문자열임 (예: `"123,456명"`)
  - 못 찾으면 `"'<title>' 은(는) <date> 순위에 없습니다."` 문자열임
- 동작 : 목록을 돌며 `movieNm`이 `title`과 같은 영화의 `audiCnt`를 정수로 바꿔 포맷함

## 참고

- 두 함수에 API 호출 코드와 목록을 꺼내는 코드가 중복됨
- `get_boxoffice_rank_1`은 목록이 비어 있으면 `IndexError`가 남
- `get_movie_audience`는 못 찾은 경우에도 문자열을 돌려주므로, 호출하는 쪽에서 성공과 실패를 구분하기 어려움
