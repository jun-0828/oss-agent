# week09

## 무엇을 하는 코드인가
영화진흥위원회(KOBIS) 오픈 API로 일별 박스오피스를 조회합니다.

- `get_boxoffice_rank_1(date)`: 그날 1위 영화 제목을 돌려줍니다.
- `get_movie_audience(date, title)`: 그날 그 영화의 관객 수(예: `"123,456명"`)를 돌려줍니다.

## 설치
```bash
pip install requests
```

같은 폴더에 `secret.py`를 만들고 KOBIS API 키를 넣습니다.
```python
API_KEY = "발급받은_키"
```

## 실행
`week09` 폴더에서 다음을 실행합니다. 날짜는 `YYYYMMDD` 형식입니다.
```bash
python -c "from tools_nodoc import *; print(get_boxoffice_rank_1('20261027'))"
```

> 파일 이름에 공백이 있으면(`tools _nodoc.py`) import할 수 없으니 먼저 `tools_nodoc.py`로 바꾸세요.
