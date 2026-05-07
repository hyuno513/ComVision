import json

# 노트북 셀 생성
cells = [
    # 기본 설정
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "setup",
        "metadata": {},
        "outputs": [],
        "source": "import warnings\nwarnings.filterwarnings(\"ignore\")\n\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report\nimport seaborn as sns\n\n# 한글 폰트 설정 (Windows)\nimport platform\nfrom matplotlib import rc\nif platform.system() == 'Windows':\n    plt.rc('font', family='Malgun Gothic')\n\n# 출력 형식 설정\nnp.set_printoptions(suppress=True, precision=4)\npd.options.display.float_format = '{:,.4f}'.format\npd.set_option('display.max_columns', None)\npd.set_option('display.max_rows', None)\nplt.rcParams['font.size'] = 14\n\nrandom_seed = 123".split('\n')
    },
    # 제목
    {
        "cell_type": "markdown",
        "id": "title",
        "metadata": {},
        "source": "# 한국교육개발원 데이터 - RandomForest 분류 모델\n고등교육기관 졸업자의 졸업 후 상황 분류 (빅데이터: 12,990행)".split('\n')
    },
    # 1단계
    {"cell_type": "markdown", "id": "sec1", "metadata": {}, "source": "## 1단계: 데이터 로드 및 기본 확인".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "load", "metadata": {}, "outputs": [], "source": "df_edu = pd.read_csv('input/한국교육개발원_고등교육기관 졸업자 학과별 졸업 후 상황_20260121.csv', encoding='euc-kr')\nprint(f'데이터 크기: {df_edu.shape}')\nprint(f'행 수: {len(df_edu)}, 컬럼 수: {df_edu.shape[1]}')\nprint()\nprint('컬럼명:')\nprint(df_edu.columns.tolist())\nprint()\nprint('데이터 첫 5행:')\nprint(df_edu.head())\nprint()\nprint('결측치 확인:')\nprint(df_edu.isnull().sum().sum())".split('\n')},
    # 2단계
    {"cell_type": "markdown", "id": "sec2", "metadata": {}, "source": "## 2단계: 탐색적 데이터 분석 (EDA)".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "eda", "metadata": {}, "outputs": [], "source": "print('데이터 기본 정보:')\nprint(df_edu.info())\nprint()\nprint('수치형 컬럼 통계:')\nprint(df_edu.describe())\nprint()\nprint('첫 번째와 두 번째 컬럼 값 샘플:')\nprint(df_edu.iloc[:, 0].value_counts().head(10))\nprint()\nprint(df_edu.iloc[:, 1].value_counts().head(10))".split('\n')},
    # 3단계
    {"cell_type": "markdown", "id": "sec3", "metadata": {}, "source": "## 3단계: 데이터 전처리 및 분류 타겟 설정".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "prep", "metadata": {}, "outputs": [], "source": "df = df_edu.copy()\nnumeric_cols = df.columns[3:]\ny = df[numeric_cols].idxmax(axis=1)\nprint('분류 타겟 (졸업 후 상황 분포):')\nprint(y.value_counts())\nprint()\nprint(f'분류 클래스 개수: {len(y.unique())}')".split('\n')},
    # 4단계
    {"cell_type": "markdown", "id": "sec4", "metadata": {}, "source": "## 4단계: 피처 엔지니어링 및 데이터 분할".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "feat", "metadata": {}, "outputs": [], "source": "X = df[numeric_cols].copy()\nX = X.fillna(0)\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed, stratify=y)\nprint(f'학습 데이터: {len(X_train)}행')\nprint(f'테스트 데이터: {len(X_test)}행')".split('\n')},
    # 5단계
    {"cell_type": "markdown", "id": "sec5", "metadata": {}, "source": "## 5단계: RandomForest 분류 모델 학습".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "train", "metadata": {}, "outputs": [], "source": "from sklearn.ensemble import RandomForestClassifier\nrf_model = RandomForestClassifier(n_estimators=100, max_depth=15, min_samples_split=5, min_samples_leaf=2, random_state=random_seed, n_jobs=-1)\nprint('모델 학습 중...')\nrf_model.fit(X_train, y_train)\nprint('✓ 모델 학습 완료!')".split('\n')},
    # 6단계
    {"cell_type": "markdown", "id": "sec6", "metadata": {}, "source": "## 6단계: 예측 및 평가".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "eval", "metadata": {}, "outputs": [], "source": "y_pred_train = rf_model.predict(X_train)\ny_pred_test = rf_model.predict(X_test)\ntrain_accuracy = accuracy_score(y_train, y_pred_train)\ntest_accuracy = accuracy_score(y_test, y_pred_test)\nprint('=== RandomForest 분류 결과 ===')\nprint(f'학습: {train_accuracy:.4f}, 테스트: {test_accuracy:.4f}')\nprint(classification_report(y_test, y_pred_test))\ncm = confusion_matrix(y_test, y_pred_test)\nprint('혼동행렬:')\nprint(cm)".split('\n')},
    # 7단계
    {"cell_type": "markdown", "id": "sec7", "metadata": {}, "source": "## 7단계: 결과 분석 및 시각화".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "feat_imp", "metadata": {}, "outputs": [], "source": "feature_importance = pd.Series(rf_model.feature_importances_, index=numeric_cols).sort_values(ascending=False)\nplt.figure(figsize=(10, 8))\nfeature_importance.head(15).plot(kind='barh', color='steelblue')\nplt.title('RandomForest - 상위 15개 피처 중요도')\nplt.tight_layout()\nplt.show()".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "cm_viz", "metadata": {}, "outputs": [], "source": "plt.figure(figsize=(10, 8))\nsns.heatmap(cm, annot=True, fmt='d', cmap='Blues')\nplt.title('혼동행렬')\nplt.tight_layout()\nplt.show()".split('\n')},
    # 8단계
    {"cell_type": "markdown", "id": "sec8", "metadata": {}, "source": "## 8단계: 추가 시각화 (Decision Tree, Learning Curve, 성능 지표)".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "tree_viz", "metadata": {}, "outputs": [], "source": "from sklearn.tree import plot_tree\nplt.figure(figsize=(20, 10))\nplot_tree(rf_model.estimators_[0], feature_names=numeric_cols.tolist(), class_names=rf_model.classes_.tolist(), filled=True, rounded=True, fontsize=10)\nplt.title('RandomForest의 첫 번째 Decision Tree 구조')\nplt.tight_layout()\nplt.show()\nprint('✓ Decision Tree 시각화 완료')".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "learn_curve", "metadata": {}, "outputs": [], "source": "from sklearn.model_selection import learning_curve\ntrain_sizes, train_scores, val_scores = learning_curve(rf_model, X_train, y_train, cv=5, n_jobs=-1, train_sizes=np.linspace(0.1, 1.0, 10), scoring='accuracy')\ntrain_mean = np.mean(train_scores, axis=1)\ntrain_std = np.std(train_scores, axis=1)\nval_mean = np.mean(val_scores, axis=1)\nval_std = np.std(val_scores, axis=1)\nplt.figure(figsize=(10, 6))\nplt.plot(train_sizes, train_mean, 'o-', color='steelblue', label='학습', linewidth=2, markersize=6)\nplt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.2, color='steelblue')\nplt.plot(train_sizes, val_mean, 's-', color='orange', label='검증', linewidth=2, markersize=6)\nplt.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.2, color='orange')\nplt.xlabel('학습 데이터 크기')\nplt.ylabel('정확도')\nplt.title('Learning Curve')\nplt.legend()\nplt.grid(True, alpha=0.3)\nplt.tight_layout()\nplt.show()\nprint('✓ Learning Curve 완료')".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "perf_metrics", "metadata": {}, "outputs": [], "source": "from sklearn.metrics import precision_recall_fscore_support\nprecision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred_test, average=None)\nfig, axes = plt.subplots(1, 3, figsize=(15, 5))\naxes[0].bar(range(len(precision)), precision, color='steelblue', alpha=0.7)\naxes[0].set_ylabel('Precision')\naxes[0].set_title('정밀도')\naxes[0].set_ylim([0, 1.0])\naxes[1].bar(range(len(recall)), recall, color='orange', alpha=0.7)\naxes[1].set_ylabel('Recall')\naxes[1].set_title('재현율')\naxes[1].set_ylim([0, 1.0])\naxes[2].bar(range(len(f1)), f1, color='green', alpha=0.7)\naxes[2].set_ylabel('F1-Score')\naxes[2].set_title('F1-Score')\naxes[2].set_ylim([0, 1.0])\nplt.suptitle('클래스별 성능 지표')\nplt.tight_layout()\nplt.show()\nprint('✓ 성능 지표 완료')".split('\n')},
    {"cell_type": "code", "execution_count": None, "id": "pred_prob", "metadata": {}, "outputs": [], "source": "y_pred_proba = rf_model.predict_proba(X_test)\nmax_proba = np.max(y_pred_proba, axis=1)\ncorrect_mask = y_pred_test == y_test\ncorrect_proba = max_proba[correct_mask]\nincorrect_proba = max_proba[~correct_mask]\nplt.figure(figsize=(12, 5))\nplt.subplot(1, 2, 1)\nplt.hist(correct_proba, bins=30, alpha=0.6, label=f'정답 ({len(correct_proba)})', color='green')\nplt.hist(incorrect_proba, bins=30, alpha=0.6, label=f'오답 ({len(incorrect_proba)})', color='red')\nplt.xlabel('예측 확률')\nplt.ylabel('빈도')\nplt.title('정답/오답 예측 확률')\nplt.legend()\nplt.subplot(1, 2, 2)\nplt.boxplot([correct_proba, incorrect_proba], labels=['정답', '오답'])\nplt.ylabel('예측 확률')\nplt.title('확률 비교')\nplt.suptitle('예측 확률 분석')\nplt.tight_layout()\nplt.show()\nprint('✓ 예측 확률 분석 완료')".split('\n')}
]

# 노트북 객체
notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.x"}
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

# 저장
with open('머신러닝0423.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print("✓ 머신러닝0423.ipynb 생성 완료! (올바른 순서: 1~7단계 → 8단계)")
