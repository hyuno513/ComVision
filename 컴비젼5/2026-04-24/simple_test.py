import sys
print("Python version:", sys.version)
print("Executable:", sys.executable)

try:
    import pandas as pd
    print("pandas: OK")
    df = pd.read_csv('input/한국철도공사_시군구단위 거주 철도이용객 이용 시간대별 소비업종 정보_20221115.csv')
    print(f"Data loaded: {df.shape}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
