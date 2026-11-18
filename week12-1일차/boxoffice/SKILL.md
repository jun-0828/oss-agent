---
name: boxoffice
description: (영화진흥위원회 사이트의 일별 박스오피스를 조회한다. 특정 날짜의 영화 순위나 관객의 인원 수를 추출할 때 사용한다.)
---

# 박스오피스 조회

영화진흥위원회 KOBIS 의 일별 박스오피스를 조회한다.

## 쓰는 법

week12 폴더에서 아래 명령을 실행한다. 날짜는 8자리(예: 20261114)로 쓴다.

- 1위 영화 제목: (1위 영화 제목 : python .claude/skills/boxoffice/scriptsboxoffice.py rank 날짜)
- 특정 영화의 관객 수: (관객 수 : python .claude/skills/boxoffice/scriptsboxoffice.py audience 관객 수)

## 지킬 것

- 스크립트가 출력한 결과만 근거로 답한다. 값을 지어내지 않는다.
- 결과가 안내 문장(자료 없음, 요청 거절 등)이면 그 내용을 그대로 전한다.
- tools.py 와 secret.py 는 읽거나 고치지 않는다. 스크립트만 실행한다.
