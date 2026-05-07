#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Option A + Option B(올바른 순서)를 통합한 노트북 생성 스크립트
"""
import json

# 기존 노트북 읽기
with open('2.의사결정나무_회귀분석.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

cells = notebook['cells']

# Option B 시작 위치 찾기
option_b_start_idx = None
for i, cell in enumerate(cells):
    if cell.get('cell_type') == 'markdown':
        source = cell.get('source', [])
        if isinstance(source, list):
            source_text = ''.join(source)
        else:
            source_text = str(source)

        if 'OPTION B' in source_text:
            option_b_start_idx = i
            break

if option_b_start_idx is None:
    print("ERROR: Option B를 찾을 수 없습니다")
    exit(1)

print(f"Option B 시작 인덱스: {option_b_start_idx}")
print(f"전체 셀 수: {len(cells)}")

# Option A와 Option B 분리
option_a_cells = cells[:option_b_start_idx]
option_b_cells = cells[option_b_start_idx:]

print(f"Option A 셀: {len(option_a_cells)}개")
print(f"Option B 셀: {len(option_b_cells)}개")

# Option B 셀들 역순 정렬 (현재 역순이므로 다시 역순으로)
option_b_cells_reversed = option_b_cells[::-1]

# 새 노트북 구성: Option A + 역순 정렬된 Option B
new_cells = option_a_cells + option_b_cells_reversed

# 새 노트북 생성
new_notebook = {
    "cells": new_cells,
    "metadata": notebook.get('metadata', {}),
    "nbformat": notebook.get('nbformat', 4),
    "nbformat_minor": notebook.get('nbformat_minor', 5)
}

# 새 파일로 저장
output_filename = '3.의사결정나무_회귀분류분석_통합.ipynb'
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(new_notebook, f, ensure_ascii=False, indent=1)

print("\n OK: 새 노트북 생성 완료!")
print(f"  파일명: {output_filename}")
print(f"  구성: Option A ({len(option_a_cells)}개) + Option B ({len(option_b_cells_reversed)}개)")
print(f"\n다음 단계:")
print(f"  1. Jupyter Notebook 실행: jupyter notebook {output_filename}")
print(f"  2. 전체 코드 실행 (Kernel > Restart & Run All)")
