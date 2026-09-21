# 개발 일지

--------------------------------------------------------------------------------------
## 2026-09-15 (1일차) — 판 깔기(시작)

### 한 것
- GitHub 레포 `physlab-analysis-pandas` 생성    
  (Public, MIT, Python .gitignore)
- Anaconda Prompt에서 `git clone`으로 내 컴퓨터
  (문서 폴더)에 복사
- VS Code로 프로젝트 폴더 열기
- 폴더 구조 생성: data/raw, data/meta, notebooks, 
  src/physlab, tests, figures, legacy, docs
- 빈 폴더마다 `.gitkeep`, src/physlab에 `__init__.py`
- v0 코드(AI 생성 Streamlit 앱, 약 2,140줄)를 `legacy/app_v0.py`로 보관
- README.md 초안 작성
- 첫 커밋 + push 성공 (커밋 2개)

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

### v0에 대한 판단
- 2,140줄 중 실제 분석 코드는 약 120줄, 나머지는 PDF 파서·교과서 텍스트·AI 채팅·UI
- 코드 의미를 전혀 모름 → 재사용하지 않음, before 증거 + 독해력 측정기로만 보관
-------------------------------------------------------------------------------------
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

- 파일오픈(plane text)
  : 파일디스크립터변수 = open(파일이름, 파일열기모드)
  * 상대경로 / 파일열기모드(r, w, a)
-> 각 인자마다 작은따옴표 각각 써주기 주의

- 파일닫기
  : 파일디스크립터변수.close()
-> 각 블록마다(읽고 쓰고 등) 꼭 닫아주고 다시 실행하기
-> 귀찮으면 with문 활용하기

- 파일읽기
  : 디스크립터.readlines(), 디스크립터.readline()
    , 디스크립터.readline()

- 파일쓰기
  : write() 함수 사용, 디스크립터.write()
    라인바꾸기->\n
-------------------------------------------------------------------------------------
## 2026-9-17

### 배운것
- csv파일 읽기
  1. 파일읽기는 마찬가지로 open함수 사용
  2. 파이썬 csv 라이브러리 이용 

- csv.reader(오픈한 파일 디스크립터, delimiter=',')
  데이터를 list로 변환하여 활용할 수 있음

- csv파일 쓰기
  1. open(디스크립터, 'w', encoding='utf-8-sig',   
     newline='')
     -> newline은 빈 라인 추가 방지용
  2. csv.reader 대신, csv.writer 함수 사용
    * 사전타입으로 파일쓰기 
      = csv.writer 함수 대신에, csv.DictWriter 함수 
        사용
        field 이름 선언 후, 데이터 넣기
      (사전타입으로 읽기도 가능 = csv.Dictreader) 

- XML 파일 포멧
  (요즘은 JSON을 쓰므로 자세히 알필욘X)
  기본구조 : <태그 속성="속성값">내용</태그>   
            태그로 열고 내용을 적고 태그로 닫음
            태그와 태그 사이에는 태그 추가 작성 가능

- XML 파일 읽기
  1. open() 함수로 xml 데이터 읽기
  data_file = open('users.xml', 'r', 
  encoding='utf-8-sig')

  2. xml 데이터 파싱하기
  soup = BeautifulSoup(data_file, 'xml') 

  3. select() 로 원하는 데이터 태그 선택하기
  users = soup.select('user')                     

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(xml파일디스크립터, 'xml')
  soup.select(원하는 데이터 태그)

  4. 리스트이므로 for 문으로 아이템 추출
     각 아이템.text 로 원하는 데이터 출력
-------------------------------------------------------------------------------------
## 2026-9-17

### 배운것
1. JSON 데이터 포멧
  - json.loads() 함수로 문자열로된 json 데이터를 사전처럼 다룰 수 있음
  - json.dumps() 함수로 파이썬 사전 데이터를 JSON 문자열 데이터로 변환할 수 있음
     (indent= 로 들여쓰기해서 보기 편하게 할 수 있음)
  - json.dump() 함수로 파이썬 사전 데이터를 파일로 쓸 수 있음
  - json.load() 함수로 파일로된 json 데이터를 사전처럼 다룰 수 있음

2. pandas 라이브러리 이해(C R U D)
  - raw data: 아직 데이터 분석을 위해 정제되지 않은 기본 데이터를 의미
     -> 데이터 전처리가 필요
  - Series
    : 1차원 데이터, 열이 1개 / index = 행의 레이블(0부터 시작, 지정가능)

    * 읽고 수정하기
      : seriesdata.index(읽기) / seriesdata.index = (변수명) (수정)
        print (seriesdata['변수명'], seriesdata.iloc[0]) (특정데이터 지정)
        del seriesdata['변수명'] (특정데이터 삭제)
    * 데이터 타입
      : object(문자열), int64(정수), float64(부동소숫점)
        bool(True 또는 False 값을 가지는 boolean)
        datetime64 (날짜/시간), timedelta[ns] (두 datatime64 간의 차) 
      : 데이터 타입 변경: Series.astype(변경할 타입)
    
  - Dataframe
    : 2차원 데이터, 열이 여러개(serise가 여러개 합쳐진 모습)

    * 생성하기 
      : df = pd.DataFrame({
        "key1": [list],
        "key2": [list],
        })
      + index를 지정해줄수도 있음.(index = [list])

    * 데이터프레임은 index, columns, values 
      df.index, df.columns, df.values

    * 인덱스로 특정 컬럼 선택하기: df = df.set_index('변수명')
      인덱스 이름: df.index.name = (변경도 가능)
    * 인덱스 데이터를 컬럼으로 변경하기: df = df.reset_index('변수명')

    * 데이터프레임 데이터 접근하기
        데이터프레임.loc : index 를 통해서 값을 찾음
        데이터프레임.iloc : 인덱스 번호를 통해서 값을 찾음 (0부터 시작)  
       
    * dataframe 컬럼 추가 : df['변수명'] = [변수]
      dataframe 컬럼 삭제 : del df['변수명']

    * 원본 데이터는 놔두고, 복사해서 데이터 처리를 하는 경우가 많음
      df2 = df[['변수1', '변수2']].copy()
 
### 한것
1. 엑셀 측정 데이터를 세로형 CSV 파일(data/electron_charge_practice.csv)로 변환
  (변환은 ai에게 시켜도 무방, 어차피 csv파일을 다루기 때문)

2. csv 파일 다루기 연습
  - Jupyter Notebook 파일 생성 (notebooks/01_electron_charge.ipynb)
  - Pandas pd.read_csv()로 데이터프레임(df) 로드
  - 파이썬 함수를 만들어 표 전체의 자기장 및 비전하 일괄 계산 완료
  - 물리 계산 로직만 따로 빼서 src/physlab/physics_calc.py 파일로 모듈화
-------------------------------------------------------------------------------------
## 2026-9-20

### 배운것
1. 탐색적 데이터 분석과정(EDA)
   - 데이터 분석을 위해 raw data를 다양한 각도에서 관찰하여, 데이터를 이해하는 과정
   - 데이터의 출처와 주제에 대해 이해
     데이터의 크기 확인
     데이터 구성 요소(feature)의 속성(특징) 확인 
     -> 3단계를 기본으로 함
   * pandas 라이브러리로 csv 파일 읽기
     csv 파일을 pandas dataframe 으로 읽기 위해 read_csv() 함수를 사용
     csv 구분자는 quotechar=구분자 옵션을 넣어서 구분자가 다른 경우도 읽기 가능
     - 관련 옵션: on_bad_lines 옵션(잘못된 행을 만났을 때 수행할 작업을 지정)
                  'error' : 잘못된 행을 만나면 에러 발생하고 중단
                  'warn' : 잘못된 행을 만나면 경고를 표시하고 해당 행을 건너뜀
                  'skip' : 잘못된 행을 만나면 에러나 경고를 표시하지 않고 건너뜀

   * 탐색적 데이터 분석: 1. 데이터의 출처와 주제에 대해 이해
   * 탐색적 데이터 분석: 2. 데이터의 크기 확인
     -> 데이터를 pandas로 읽은 후, 가장 먼저 하는 일 : 데이터 일부 확인하기
        head(): 처음 5개(디폴트)의 데이터 확인하기
        tail(): 마지막 5개의 데이터 확인하기
        shape: 데이터의 row, column 사이즈 확인
        info(): column별 데이터 타입과 실제 데이터가 있는 사이즈 확인
   * 탐색적 데이터 분석: 3. 데이터 구성 요소(feature)의 속성(특징) 확인
     1) 각 column 이해하기
     2) 속성이 숫자라면, 평균, 표준편차, 4분위 수, 최소/최대값 확인하기
        (count: 갯수, mean: 평균, std: 표준편차, min: 최소값, max: 최대값)
     3) 속성간 상관관계 이해하기(피어슨 상관관계/양, 음, 0)
        (doc.corr(numeric_only=True))
      -> 주요데티어 시각화(최근에는 plotly 사용)  
         plotly 라이브러리 임포트: import plotly.express as px
         상관계수 행렬 계산: corr = doc.corr(numeric_only=True) 
         fig = px.imshow(
            corr,                           # 계산된 상관계수 객체
            text_auto=True,                 # 각 셀에 상관계수 값 표시
            color_continuous_scale='Blues', # 색상 스케일 지정
            zmin=-1, zmax=1,                # 상관계수 범위 (-1 ~ 1)
            width=800, height=600           # 그래프의 가로, 세로 크기
          )
         fig.show()                         # 생성된 그래프 객체를 화면에 출력

     4) Series 로 feature를 보다 상세하게 탐색하기
          size : 사이즈 반환
          count() : 데이터가 없는 경우를 뺀 사이즈 반환
          unique(): 유일한 값만 반환
          value_counts(): 데이터가 없는 경우를 제외하고, 각 값의 갯수를 반환  

2. pandas 라이브러리로 데이터 처리하기
  1) 필요한 컬럼만 선택하기 -> 변수명 = doc[['컬럼', '컬럼']] 
  2) 특정 조건에 맞는 row 검색하기 -> doc_us = doc[doc['칼럼'] == '칼럼명']
  3) 없는 데이터(NaN, 결측치) 처리하기
          없는 데이터(결측치) 가 있는지 확인하기
          isnull() : 없는 데이터가 있는지 확인 (True or False)
          sum() : 없는 데이터가 있는 행의 갯수 확인
          -> 통상 isnull().sum() 으로 사용
          -> 없는 데이터 삭제하기 = doc.dropna() : 결측치를 가진 행을 모두 삭제
          -> 특정 컬럼값이 없는 데이터만 삭제하기 : subset으로 해당 컬럼을 지정해줌
             (doc = doc.dropna(subset=['컬럼명']))
          -> 없는 데이터(NaN)을 특정값으로 일괄 변경하기
             (doc.fillna(특정값) : 특정값으로 결측치를 대체)
          -> 없는 데이터(NaN)중 특정 컬럼에 대해 특정 값으로 일괄 변경하기
             (nan_data = {'컬럼1': 0, '컬럼2':0}
              doc = doc.fillna(nan_data))     
  4) 특정 키값을 기준으로 데이터 합치기
      groupby() : SQL 구문의 group by 와 동일, 특정 컬럼을 기준으로 그룹
      sum() : 그룹으로 되어 있는 데이터를 합치기
      doc = doc.groupby('칼럼명').sum()
  5) 데이터프레임에서 중복 행 확인/제거하기
      duplicated() : 중복 행 확인하기
      drop_ducplicates() : 중복 행 삭제중복값
        - 특정 컬럼을 기준으로 중복 행 제거하기
            subset=특정컬럼
        - 중복된 경우, 처음과 마지막 행 중 어느 행을 남길 것인지 결정하기
            처음: keep='first' (디폴트)
            처음: keep='last'

3. DataFrame 간 연결/병합해서 데이터 가공하기
  - concat(): 두 데이터프레임을 연결해서 하나의 데이터프레임으로 만들 수 있음
    = pd.concat([데이터프레임1, 데이터프레임2])
    axis: 0 이면(디폴트) 위에서 아래로 합치고, 1 이면 왼쪽과 오른쪽으로 합침
    = pd.concat([df1, df2], axis=1)

  - merge(데이터프레임1, 데이터프레임2) : 두 데이터프레임에 동일한 이름을 가진 컬럼을  
                                        기준으로 두 데이터프레임을 합침
   = pd.merge(df1, df2)
   * merge 여러가지 결합방법
      inner : 내부 조인
      outer : 완전 외부 조인
      left : 왼쪽 우선 외부 조인
      right : 오른쪽 우선 외부 조인
      (= merge(데이터프레임1, 데이터프레임2, how=결합방법))
      
-------------------------------------------------------------------------------------
## 2026-9-21

### 배운것
- 데이터 시각화
  : 칼럼이 다른 경우가 대부분 -> 특정칼럼만 선택해서 DataFrame 만들기 
    + try except 구문이용

  : 데이터프레임 데이터 변환하기
     1. 특정 컬럼만 선택해서 데이터프레임 만들기
     2. 특정 컬럼에 없는 데이터 삭제하기
     3. 특정 컬럼의 데이터 타입 변경하기  

- 실전으로 들어가니까 어려워지기시작함!!!  

-------------------------------------------------------------------------------------
## 2026-9-22

### 배운것   