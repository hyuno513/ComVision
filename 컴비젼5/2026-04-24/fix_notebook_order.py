import json

# 노트북 파일 읽기
with open('2.의사결정나무_회귀분석.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

cells = notebook['cells']

# Option B 부분 찾기 (OPTION B가 포함된 마크다운 셀부터 끝까지)
option_b_start = None
option_a_end = None

for i, cell in enumerate(cells):
    if cell['cell_type'] == 'markdown':
        if 'OPTION B' in str(cell.get('source', '')):
            option_b_start = i
            break

print(f"Option B 시작 인덱스: {option_b_start}")
print(f"전체 셀 수: {len(cells)}")

if option_b_start is None:
    print("Option B를 찾을 수 없습니다.")
    exit(1)

# Option B 부분 추출 (OPTION B 시작부터 끝까지)
option_b_cells = cells[option_b_start:]
option_a_cells = cells[:option_b_start]

print(f"\nOption A 셀: {len(option_a_cells)}개")
print(f"Option B 셀: {len(option_b_cells)}개")

# Option B의 올바른 순서 정의
# 현재 역순이므로 역순으로 뒤집기
option_b_cells_fixed = option_b_cells[::-1]

# 검증: 처음과 마지막 셀 확인
print(f"\n수정 전 Option B:")
print(f"  첫 번째: {option_b_cells[0].get('source', [''])[0][:50]}")
print(f"  마지막: {option_b_cells[-1].get('source', [''])[0][:50]}")

print(f"\n수정 후 Option B:")
print(f"  첫 번째: {option_b_cells_fixed[0].get('source', [''])[0][:50]}")
print(f"  마지막: {option_b_cells_fixed[-1].get('source', [''])[0][:50]}")

# 새로운 노트북 구성
notebook['cells'] = option_a_cells + option_b_cells_fixed

# 수정된 노트북 저장
with open('2.의사결정나무_회귀분석.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print("\n✓ 노트북 셀 순서 수정 완료!")
print("  파일: 2.의사결정나무_회귀분석.ipynb")
