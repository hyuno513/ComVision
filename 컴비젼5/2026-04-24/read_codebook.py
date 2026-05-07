import pandas as pd

# 코드북 읽기
codebook_path = 'input/시군구단위 거주 철도이용객 이용 시간대별 소비업종 정보_코드북.xlsx'

try:
    # 모든 시트 읽기
    xls = pd.ExcelFile(codebook_path, engine='openpyxl')
    print("코드북 시트 목록:")
    for sheet in xls.sheet_names:
        print(f"  - {sheet}")

    print("\n" + "="*70)
    for sheet in xls.sheet_names:
        print(f"\n[{sheet}]")
        df = pd.read_excel(codebook_path, sheet_name=sheet, engine='openpyxl')
        print(df.to_string())
        print()

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
