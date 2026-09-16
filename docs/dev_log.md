# 개발 일지

형식: 날짜 / 한 것 / 처음 해본 것 / 배운 것 / 막힌 것과 해결 / 다음

---

## 2026-09-15 (1일차) — 판 깔기(시작)

### 한 것
- GitHub 레포 `physlab-analysis-pandas` 생성 (Public, MIT, Python .gitignore)
- Anaconda Prompt에서 `git clone`으로 내 컴퓨터(문서 폴더)에 복사
- VS Code로 프로젝트 폴더 열기
- 폴더 구조 생성: data/raw, data/meta, notebooks, src/physlab, tests, figures, legacy, docs
- 빈 폴더마다 `.gitkeep`, src/physlab에 `__init__.py`
- v0 코드(AI 생성 Streamlit 앱, 약 2,140줄)를 `legacy/app_v0.py`로 보관
- README.md 초안 작성
- 첫 커밋 + push 성공 (커밋 2개)

### 처음 해본 것
- 터미널(Anaconda Prompt) 사용: cd, dir, git --version, git clone
- git / GitHub: clone, add(+), commit, push(동기화)
- VS Code: 폴더 열기, 탐색기에서 파일·폴더 생성, 소스 제어 탭
- GitHub 인증 (Git Credential Manager 브라우저 로그인)

### 배운 것
- 터미널 명령 / 파이썬 코드 / 텍스트 파일은 입력하는 곳이 다르다
  (conda, git → 터미널 / import → 노트북 셀 / 폴더 구조 그림 → 입력 아님)
  -> 아직 이해가 부족하므로 추가로 알아볼 필요있음!
- `%USERPROFILE%`은 윈도우가 자동으로 C:\Users\내이름 으로 바꿔준다
- clone은 GitHub에 레포가 먼저 있어야 된다 ("Repository not found" = 레포 없음)
- git은 빈 폴더를 저장하지 않는다 → `.gitkeep`
- `.git` 폴더는 git 내부 저장소, 절대 건드리지 않는다
- VS Code에서 새 파일은 Enter 순간 저장됨 → 빈 파일에 Ctrl+S는 변화 없음이 정상
- 탭 이름 옆 흰 점(●) = 저장 안 됨
- 파일 옆 초록 U = Untracked (git에 아직 안 담긴 새 파일)
- 커밋 = 스냅샷 + 메시지. 메시지는 "수정" 말고 "무엇을 했는지"
- 커밋 리듬: 작업 하나 → Ctrl+S → + → 메시지 → 커밋 → 동기화

### 막힌 것과 해결
- Jupyter 셀에 conda 명령 입력 → SyntaxError → 터미널에 입력해야 함
- 경로 없음 문구→ `%USERPROFILE%` 사용
- git clone "not found" → GitHub에 레포 미생성 → 레포 먼저 만들고 재시도
- `code .` 인식 안 됨 → VS Code 메뉴 파일→폴더 열기로 대체
- VS Code에서 `.git` 폴더를 열어버림 → 상위 폴더 다시 열기

### v0에 대한 판단
- 2,140줄 중 실제 분석 코드는 약 120줄, 나머지는 PDF 파서·교과서 텍스트·AI 채팅·UI
- 코드 의미를 전혀 모름 → 재사용하지 않음, before 증거 + 독해력 측정기로만 보관

### 다음
- .gitignore 보강, conda env physlab, requirements.txt, 00_setup_check.ipynb
- docs/why_v0_failed.md, docs/ai_rules.md
- 주말: 과거 실험 보고서 → 첫 CSV(세로형) + meta

## 2026-9-16

### 한것
- 앞으로의 프로젝트 기반다지기
  1. 규칙 정하기
  2. 성장했다는 판단 기준 세우기/v0실패 이유 적기
  3. 커밋 방법 익히기

### 배운것
- 커밋 무한 렉
  : 보통 커밋 메시지를 안 적고 커밋 버튼을 눌러서    
    백그라운드에서 메시지 입력창을 기다리느라 뻗었거나, 깃허브 로그인 창이 뒤에 숨어있을 때 발생
    ->Vs Code를 껐다 키고, -버튼(스테이징 취소) 활용
- 커밋할 때는 하나씩 커밋하기
  (+버튼->메세지 작성->커밋)    
- 커밋할 때 -> +버튼 = 택배박스에 포장
           -> 메세지 작성 = 라벨스티커(작업이름메모)
           -> 커밋 = 밀봉해서 창고에 넣기 
- .gitkeep의 역할 = 텅빈 파일을 넣어 Github에 새로운 파일들을 올릴수 있도록 하는 것