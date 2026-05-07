import json

# 기존 노트북 읽기
with open('2.의사결정나무_회귀분석.ipynb', 'r', encoding='utf-8') as f:
    old_notebook = json.load(f)

old_cells = old_notebook['cells']

# Option B 시작 인덱스 찾기
option_b_start = None
for i, cell in enumerate(old_cells):
    if cell['cell_type'] == 'markdown':
        source = cell.get('source', [])
        if isinstance(source, list):
            source_text = ''.join(source)
        else:
            source_text = str(source)

        if 'OPTION B' in source_text:
            option_b_start = i
            break

print(f"Option B 시작 인덱스: {option_b_start}")

# Option A 부분만 추출
option_a_cells = old_cells[:option_b_start]
print(f"Option A 셀 수: {len(option_a_cells)}")

# 새 노트북 구조 생성
new_notebook = {
    "cells": option_a_cells,
    "metadata": old_notebook.get('metadata', {}),
    "nbformat": old_notebook.get('nbformat', 4),
    "nbformat_minor": old_notebook.get('nbformat_minor', 5)
}

# 새 파일로 저장
with open('3.의사결정나무_회귀분류분석_통합.ipynb', 'w', encoding='utf-8') as f:
    json.dump(new_notebook, f, ensure_ascii=False, indent=1)

print("✓ 기본 파일 생성 완료: 3.의사결정나무_회귀분류분석_통합.ipynb")
print("  (Option A 부분만 포함됨)")
print("\n다음 단계: Python 스크립트로 Option B를 올바른 순서로 추가합니다.")
