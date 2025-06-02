import json
import re
import pandas as pd

# JSON 파일 로드
file_path = "seoul.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# DataFrame 변환
df = pd.DataFrame(data)

before_count = len(df)

# 가격 변환 함수 정의
def convert_price(price_str, transaction_type):
    if pd.isna(price_str) or price_str is None:
        return None

    price_str = price_str.replace(",", "").replace(" ", "")  # 공백, 쉼표 제거

    if transaction_type in ["매매", "전세"]:
        match = re.search(r"(\d+)억(?:\s*(\d+))?", price_str)
        if match:
            billion = int(match.group(1)) * 10000  # 억 단위 변환
            million = int(match.group(2)) if match.group(2) else 0  # 만 단위 변환
            return int(billion + million)  # 정수 변환
        return None
    
    elif transaction_type == "월세":
        try:
            deposit, rent = price_str.split("/")
            deposit_match = re.search(r"(\d+)억(?:\s*(\d+))?", deposit)
            if deposit_match:
                billion = int(deposit_match.group(1)) * 10000
                million = int(deposit_match.group(2)) if deposit_match.group(2) else 0
                deposit_amount = int(billion + million)
            else:
                deposit_amount = int(re.sub(r"[^\d]", "", deposit))

            rent_amount = int(re.sub(r"[^\d]", "", rent))
            return deposit_amount, rent_amount
        except:
            return None, None

    return None

# 관리비 변환 함수 정의
def convert_maintenance_fee(fee_str):
    if pd.isna(fee_str) or fee_str is None:
        return None
    
    fee_str = fee_str.replace("\n", " ").strip()  # 개행 제거

    if "확인 어려움" in fee_str:
        return None
    if "없음" in fee_str or "0원" in fee_str:
        return 0

    match = re.search(r"(\d+)(?:만)?원?", fee_str)
    if match:
        return int(match.group(1)) * 10000  # 정수 변환 후 만원 단위 변환

    return None

# 가격 변환 적용
df["매매가(만원)"] = df.apply(lambda row: convert_price(row["가격"], row["거래유형"]) if row["거래유형"] in ["매매", "전세"] else None, axis=1)
df["보증금(만원)"], df["월세(만원)"] = zip(*df.apply(lambda row: convert_price(row["가격"], row["거래유형"]) if row["거래유형"] == "월세" else (None, None), axis=1))

# 관리비 변환 적용
df["관리비"] = df["관리비"].apply(convert_maintenance_fee)

# 중복 제거 (소재지, 해당층/총층, 가격, 방향 동일한 경우 제거)
df.drop_duplicates(subset=["소재지", "해당층/총층", "가격", "방향"], keep="first", inplace=True)

after_count = len(df)



# NaN을 None으로 변환하여 JSON 저장
df = df.where(pd.notna(df), None)  # NaN 값을 None으로 변환

# 숫자 컬럼을 정수(int)로 변환 (소수점 없애기)
numeric_columns = ["매매가(만원)", "보증금(만원)", "월세(만원)", "관리비"]
df[numeric_columns] = df[numeric_columns].astype("Int64")  # NaN을 유지하면서 int 변환

# JSON 파일 저장 (ensure_ascii=False 옵션 사용)
processed_file_path = "seoul_cleaned_pandas.json"
with open(processed_file_path, "w", encoding="utf-8") as file:
    json.dump(df.to_dict(orient="records"), file, ensure_ascii=False, indent=4, default=str)

print(f"변환 및 중복 제거된 데이터가 {processed_file_path} 파일에 저장되었습니다.")
