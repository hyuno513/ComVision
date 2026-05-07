# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

컴비젼 시리즈의 5번째 학습 저장소로, 머신러닝(컴비젼4)에 이어 심화 학습을 진행하는 공간입니다. 파일은 날짜별 폴더(`YYYY-M-D/`) 안에 순서 번호를 앞에 붙인 파일명(`1.주제명.ipynb`, `2.주제명.py`)으로 저장합니다.

### 컴비젼 시리즈 전체 흐름

| 폴더 | 기간 | 주요 내용 |
|------|------|-----------|
| 컴비젼1 | 2025-12 | Python 기초 (변수, 자료형, 딕셔너리, 출력 포맷) |
| 컴비젼2 | 2026-01 | 파일 입출력, CSV 처리 |
| 컴비젼3 | 2026-02~03 | numpy, pandas, matplotlib, seaborn, 데이터 분석 |
| 컴비젼4 | 2026-03~04 | 머신러닝 이론, sklearn, 분류/회귀, 의사결정나무 |
| 컴비젼5 | 2026-04~ | 심화 머신러닝 / 딥러닝 (진행 중) |

## 개발 환경

- Python 3.x + Jupyter Notebook (`.ipynb`) 또는 `.py`
- 주요 라이브러리: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`

Jupyter 실행:
```bash
jupyter notebook
```

특정 노트북 실행:
```bash
jupyter nbconvert --to notebook --execute "날짜폴더/파일명.ipynb"
```

## 모든 노트북 공통 초기 코드 (보일러플레이트)

새 노트북을 만들 때 첫 번째 셀에 아래 코드를 그대로 사용합니다.

```python
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import platform
from matplotlib import rc

if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    rc('font', family='Malgun Gothic')

from IPython.display import Image

np.set_printoptions(suppress=True, precision=4)
pd.options.display.float_format = '{:,.4f}'.format
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
plt.rcParams['font.size'] = 14

random_seed = 123
```

## 컴비젼4에서 다룬 머신러닝 핵심 개념

컴비젼5 작업 시 컴비젼4 내용을 전제로 합니다.

- **학습 방식**: 지도학습(분류·회귀·시계열), 비지도학습, 강화학습
- **데이터 전처리**: 결측치 처리(`isnull().sum()`), 인코딩, 데이터 분할(`train_test_split`)
- **알고리즘**: 의사결정나무(`DecisionTreeClassifier`), 로지스틱 회귀
- **연습 데이터셋**: 아이리스(분류), 타이타닉(분류), 유방암(이진분류), 성인소득(adult.csv)
- **평가 지표**: 정확도(accuracy), 혼동행렬(confusion matrix)
- **시각화**: 산점도(`scatterplot`), 히스토그램(`.hist()`), 의사결정나무 시각화(`graphviz`)

## 폴더 및 파일 규칙

```
컴비젼5/
├── YYYY-M-D/
│   ├── 1.주제명.ipynb
│   ├── 2.주제명.ipynb
│   ├── input/      # 원본 데이터 (CSV, Excel 등)
│   ├── data/       # 전처리된 중간 데이터
│   └── output/     # 결과물 (그래프 이미지, 모델 파일 등)
└── memo.txt
```
