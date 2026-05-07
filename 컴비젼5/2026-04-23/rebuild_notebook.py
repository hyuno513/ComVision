import json

# 노트북 로드
nb_path = "머신러닝모델423.ipynb"
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 새로운 셀 구조
cells = []

# 1. 기본 설정 (사용자 제시 코드)
setup_source = """import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import seaborn as sns

# 한글 폰트 설정 (Windows)
import platform
from matplotlib import rc
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')

# 출력 형식 설정
np.set_printoptions(suppress=True, precision=4)
pd.options.display.float_format = '{:,.4f}'.format
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
plt.rcParams['font.size'] = 14

random_seed = 123"""

cells.append({
    "cell_type": "code",
    "id": "setup_cell",
    "source": [line + '\n' for line in setup_source.split('\n')[:-1]] + [setup_source.split('\n')[-1]],
    "metadata": {},
    "execution_count": None,
    "outputs": []
})

# 2. 제목: 1단계
cells.append({
    "cell_type": "markdown",
    "id": "section_1",
    "source": ["## 1단계: 데이터 로드 및 확인"],
    "metadata": {}
})

# 3. 데이터 로드
data_load_source = """# 데이터 로드
df = pd.read_csv('input/경상북도문화관광공사_보문관광단지 내외국인 관광객 통계_20251231.csv', encoding='utf-8')

# 컬럼명 설정
df.columns = ['날짜', '관광객1', '관광객2', '관광객3', '관광객4',
              '관광객5', '관광객6', '관광객7', '관광객8', '전체관광객수']

# 기본 데이터 확인
print(f'데이터 크기: {df.shape}')
print(f'기간: {df["날짜"].iloc[0]} ~ {df["날짜"].iloc[-1]}')
print()
print('결측치:')
print(df.isnull().sum())
print()
print('데이터 첫 5행:')
print(df.head())"""

cells.append({
    "cell_type": "code",
    "id": "data_load",
    "source": [line + '\n' for line in data_load_source.split('\n')[:-1]] + [data_load_source.split('\n')[-1]],
    "metadata": {},
    "execution_count": None,
    "outputs": []
})

# 4. 제목: 2단계
cells.append({
    "cell_type": "markdown",
    "id": "section_2",
    "source": ["## 2단계: 탐색적 데이터 분석 (EDA)"],
    "metadata": {}
})

# 5. 데이터 시각화 및 통계
eda_source = """# 월별 전체 관광객 수 추이 시각화
plt.figure(figsize=(14, 5))
plt.plot(range(len(df)), df['전체관광객수'], linewidth=2, color='steelblue', marker='o', markersize=3)
plt.title('경상북도 보문관광단지 월별 전체 관광객 수 추이')
plt.xlabel('월')
plt.ylabel('관광객 수')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 데이터 통계
print('전체관광객수 통계:')
print(df['전체관광객수'].describe())"""

cells.append({
    "cell_type": "code",
    "id": "eda",
    "source": [line + '\n' for line in eda_source.split('\n')[:-1]] + [eda_source.split('\n')[-1]],
    "metadata": {},
    "execution_count": None,
    "outputs": []
})

# 6. 제목: 3단계
cells.append({
    "cell_type": "markdown",
    "id": "section_3",
    "source": ["## 3단계: 데이터 준비 (피처/타겟 설정 및 분할)"],
    "metadata": {}
})

# 7. 피처/타겟 설정 및 분할
data_prep_source = """# 피처와 타겟 설정
# 입력: 각 범주별 관광객 수 (관광객1~8)
# 출력: 전체관광객수

feature_cols = ['관광객1', '관광객2', '관광객3', '관광객4',
                '관광객5', '관광객6', '관광객7', '관광객8']
X = df[feature_cols]
y = df['전체관광객수']

# 시간 순서 유지 - 앞 80%를 학습, 뒤 20%를 테스트
split_idx = int(len(df) * 0.8)
X_train = X.iloc[:split_idx]
X_test = X.iloc[split_idx:]
y_train = y.iloc[:split_idx]
y_test = y.iloc[split_idx:]

print(f'전체 데이터: {len(df)}행')
print(f'학습 데이터: {len(X_train)}행 ({df["날짜"].iloc[0]} ~ {df["날짜"].iloc[split_idx-1]})')
print(f'테스트 데이터: {len(X_test)}행 ({df["날짜"].iloc[split_idx]} ~ {df["날짜"].iloc[-1]})')
print()
print('Y(전체관광객수) 통계:')
print(f'학습 데이터: 평균={y_train.mean():.0f}, 최소={y_train.min():.0f}, 최대={y_train.max():.0f}')
print(f'테스트 데이터: 평균={y_test.mean():.0f}, 최소={y_test.min():.0f}, 최대={y_test.max():.0f}')"""

cells.append({
    "cell_type": "code",
    "id": "data_prep",
    "source": [line + '\n' for line in data_prep_source.split('\n')[:-1]] + [data_prep_source.split('\n')[-1]],
    "metadata": {},
    "execution_count": None,
    "outputs": []
})

# 8. 제목: 4단계
cells.append({
    "cell_type": "markdown",
    "id": "section_4",
    "source": ["## 4단계: 모델 학습 (의사결정나무 회귀)"],
    "metadata": {}
})

# 9. 모델 학습
training_source = """from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import math

# 의사결정나무 회귀 모델 학습
dt_model = DecisionTreeRegressor(max_depth=5, random_state=random_seed)
dt_model.fit(X_train, y_train)

# 예측
y_pred = dt_model.predict(X_test)

print('모델 학습 완료!')
print(f'모델 파라미터: max_depth=5, random_state={random_seed}')"""

cells.append({
    "cell_type": "code",
    "id": "model_training",
    "source": [line + '\n' for line in training_source.split('\n')[:-1]] + [training_source.split('\n')[-1]],
    "metadata": {},
    "execution_count": None,
    "outputs": []
})

# 10. 제목: 5단계
cells.append({
    "cell_type": "markdown",
    "id": "section_5",
    "source": ["## 5단계: 예측 및 평가"],
    "metadata": {}
})

# 11. 평가
evaluation_source = """# 평가 지표 계산
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print('=== 의사결정나무 회귀 결과 ===')
print(f'평균절대오차(MAE):  {mae:,.0f}')
print(f'평균제곱오차(MSE):  {mse:,.0f}')
print(f'루트평균제곱오차(RMSE): {rmse:,.0f}')
print(f'결정계수(R²):      {r2:.4f}')
print()
print('테스트 데이터의 실제값 vs 예측값:')
result_df = pd.DataFrame({
    '날짜': df['날짜'].iloc[split_idx:].values,
    '실제값': y_test.values,
    '예측값': y_pred.astype(int),
    '오차': (y_test.values - y_pred).astype(int),
    '오차율': ((y_test.values - y_pred) / y_test.values * 100).round(2)
})
print(result_df.to_string(index=False))"""

cells.append({
    "cell_type": "code",
    "id": "evaluation",
    "source": [line + '\n' for line in evaluation_source.split('\n')[:-1]] + [evaluation_source.split('\n')[-1]],
    "metadata": {},
    "execution_count": None,
    "outputs": []
})

# 12. 제목: 6단계
cells.append({
    "cell_type": "markdown",
    "id": "section_6",
    "source": ["## 6단계: 결과 분석 및 시각화"],
    "metadata": {}
})

# 13. 피처 중요도
importance_source = """# 피처 중요도 시각화
importance = pd.Series(dt_model.feature_importances_, index=feature_cols)
importance.sort_values(ascending=True).plot(kind='barh', figsize=(8, 4), color='steelblue')
plt.title('의사결정나무 - 피처 중요도')
plt.xlabel('중요도')
plt.tight_layout()
plt.show()"""

cells.append({
    "cell_type": "code",
    "id": "feature_importance",
    "source": [line + '\n' for line in importance_source.split('\n')[:-1]] + [importance_source.split('\n')[-1]],
    "metadata": {},
    "execution_count": None,
    "outputs": []
})

# 14. 예측값 비교 시각화
comparison_source = """# 예측 vs 실제 비교 시각화
plt.figure(figsize=(14, 5))
x_pos = range(len(y_test))
plt.plot(x_pos, y_test.values, label='실제값', marker='o', linewidth=2, markersize=6, color='steelblue')
plt.plot(x_pos, y_pred, label='예측값', marker='s', linewidth=2, markersize=6, color='orange', alpha=0.7)
plt.title('테스트 기간: 전체관광객수 실제값 vs 예측값')
plt.xlabel('테스트 데이터 인덱스')
plt.ylabel('관광객 수')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()"""

cells.append({
    "cell_type": "code",
    "id": "prediction_comparison",
    "source": [line + '\n' for line in comparison_source.split('\n')[:-1]] + [comparison_source.split('\n')[-1]],
    "metadata": {},
    "execution_count": None,
    "outputs": []
})

# 15. 잔차 분석
residual_source = """# 잔차(오차) 시각화
residuals = y_test.values - y_pred
plt.figure(figsize=(14, 5))
plt.bar(range(len(residuals)), residuals, color=['green' if r > 0 else 'red' for r in residuals], alpha=0.6)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.title('테스트 기간: 잔차(실제값 - 예측값)')
plt.xlabel('테스트 데이터 인덱스')
plt.ylabel('잔차')
plt.tight_layout()
plt.show()"""

cells.append({
    "cell_type": "code",
    "id": "residual_analysis",
    "source": [line + '\n' for line in residual_source.split('\n')[:-1]] + [residual_source.split('\n')[-1]],
    "metadata": {},
    "execution_count": None,
    "outputs": []
})

# 노트북 재구성
nb['cells'] = cells

# 저장
with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("✅ 노트북 재배열 완료!")
print(f"총 {len(cells)}개 셀 생성됨")
