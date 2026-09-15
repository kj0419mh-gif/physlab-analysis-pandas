# physlab-analysis-pandas

학부 물리실험 데이터를 재현 가능하게 분석하기 위한 Python 도구 (진행 중).

## 문제
조별 실험 분석이 개인별 도구(엑셀/AI)에 따라 결과가 달라지고,
오차율 외의 통계(불확도, χ², 잔차)가 리포트에서 빠짐.

## 접근
원본 CSV + 메타데이터 보존 → numpy/scipy로 피팅·불확도·이상치 → 리포트 결과와 재비교.

## 폴더 구조
- `data/raw/` 원본 측정 CSV (수정하지 않음)
- `data/meta/` 실험별 단위·분해능·조건·리포트 결과 기록
- `notebooks/` 분석 노트북
- `src/physlab/` 재사용 함수
- `tests/` 함수 검증
- `figures/` 결과 그림
- `legacy/` v0 (AI 생성 초판, 참고용)
- `docs/` 문서

## 프로젝트 이력
- v0 (`legacy/app_v0.py`): AI가 전부 생성한 Streamlit 앱. 재사용하지 않음.
- v1: 진행 중

## 결과
(채워 넣을 것)

## 한계
(채워 넣을 것)
