import json
import re

# JSON 파일 로드
file_path = "오피스텔_서울.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

before_count = len(data)

# 가격 변환 함수 정의
def convert_price(price_str, transaction_type):
    """
    매매가 및 월세 데이터를 변환하여 만원 단위로 반환.
    """
    if transaction_type in ["매매", "전세"]:
        # 숫자만 남기고 공백과 쉼표 제거
        price_str = price_str.replace(",", "").replace(" ", "")
        match = re.search(r"(\d+)억(?:\s*(\d+))?", price_str)
        if match:
            billion = int(match.group(1)) * 10000  # 억 단위 변환
            million = int(match.group(2)) if match.group(2) else 0  # 만 단위 변환
            return billion + million  # 만원 단위로 변환
    
    elif transaction_type == "월세":
        # 숫자만 남기고 공백과 쉼표 제거
        price_str = price_str.replace(",", "").replace(" ", "")
        deposit, rent = price_str.split("/")
        deposit_match = re.search(r"(\d+)억(?:\s*(\d+))?", deposit)
        if deposit_match:
            billion = int(deposit_match.group(1)) * 10000
            million = int(deposit_match.group(2)) if deposit_match.group(2) else 0
            deposit_amount = billion + million
        else:
            deposit_amount = int(re.sub(r"[^\d]", "", deposit))
        
        rent_amount = int(re.sub(r"[^\d]", "", rent))
        return deposit_amount, rent_amount
    
    return None

# 관리비 변환 함수 정의
def convert_maintenance_fee(fee_str):
    """관리비 데이터를 정제하여 숫자 형태로 변환."""
    fee_str = fee_str.replace("\n", " ").strip()  # 개행 제거 및 앞뒤 공백 정리

    if "확인 어려움" in fee_str:
        return None  # 확인 어려움 -> Null 값 처리
    if "없음" in fee_str or "0원" in fee_str:
        return 0  # 없음 또는 0원 -> 0으로 변환

    match = re.search(r"(\d+)(?:만)?원?", fee_str)
    if match:
        return int(match.group(1))*10000 

    return None # 변환 불가능한 경우 None 처리

# 중복 매물 제거 함수
def remove_duplicates(data):
    """소재지, 해당층/총층, 가격, 방향까지 동일하면 중복 제거."""
    seen = set()
    unique_data = []
    removed_count = 0

    for item in data:
        key = (
            item.get('소재지', '').strip(),
            item.get('해당층/총층', '').strip(),
            item.get('가격', '').strip(),
            item.get('방향', '').strip()
        )

        if key not in seen:
            seen.add(key)
            unique_data.append(item)
        else:
            removed_count += 1
            # print(f"중복 제거된 매물번호: {item.get('매물번호')}")

    print(f"제거된 중복 매물 개수: {removed_count}개")
    return unique_data

# 변환된 데이터 저장
processed_data = []

for item in data:
    transaction_type = item.get("거래유형")
    price_str = item.get("가격", "")
    fee_str = item.get("관리비", "")

    sale_price, deposit, rent = None, None, None

    if transaction_type in ["매매", "전세"]:
        sale_price = convert_price(price_str, transaction_type)
    elif transaction_type == "월세":
        deposit, rent = convert_price(price_str, transaction_type)

    # 변환된 값을 추가
    item["매매가(만원)"] = sale_price if sale_price else None
    item["보증금(만원)"] = deposit if deposit else None
    item["월세(만원)"] = rent if rent else None
    item["관리비"] = convert_maintenance_fee(fee_str)
    processed_data.append(item)

# 중복 데이터 제거
unique_data = remove_duplicates(processed_data)

print(len(unique_data))

# 변환된 데이터 저장
processed_file_path = "officetel_cleaned.json"
with open(processed_file_path, "w", encoding="utf-8") as file:
    json.dump(unique_data, file, ensure_ascii=False, indent=4)

print(f"변환 및 중복 제거된 데이터가 {processed_file_path} 파일에 저장되었습니다.")