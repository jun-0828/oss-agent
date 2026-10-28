
"""박스오피스 정보를 가져오는 도구 모음"""

import requests
from secret import API_KEY

BASE_URL = (
    "https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
    "boxoffice/searchDailyBoxOfficeList.json"
)


def get_boxoffice_rank_1(date):
    """지정한 날짜의 박스오피스 1위 영화 제목을 반환한다."""
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

    return movies[0]["movieNm"]


def get_movie_audience(date, title):
    """지정한 날짜와 영화 제목에 해당하는 관객 수 문자열을 반환한다."""
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

    for movie in movies:
        if movie["movieNm"] == title:
            audience = int(movie["audiCnt"])
            return f"{audience:,}명"

    return f"'{title}' 은(는) {date} 순위에 없습니다."
