from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_autoinstaller
import pandas as pd
import time
import re
import json
import os
import random

# ✅ ChromeDriver 자동 설치
chromedriver_autoinstaller.install()

# ✅ 다양한 User-Agent 리스트
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
]

# ✅ Selenium 옵션 설정
options = Options()
options.add_argument("--headless=new")  # ✅ 최신 headless 모드 적용
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-gpu")  # ✅ GPU 비활성화 (렌더링 문제 방지)
options.add_argument("--disable-software-rasterizer")  # ✅ 렌더링 문제 방지
options.add_argument("--log-level=3")  # ✅ 불필요한 로그 숨기기
options.add_argument(f"user-agent={random.choice(user_agents)}")  # ✅ User-Agent 랜덤 적용

# ✅ WebDriver 실행
service = Service()
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)  # 🔥 요소 로딩을 기다리는 시간 설정

# ✅ WebDriver 탐지 방지 코드 실행
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

def load_json(filename):
    """기존 JSON 파일을 로드하는 함수"""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def save_data_to_json(filename, new_data):
    """새로운 데이터를 기존 JSON 파일에 추가하는 함수"""
    existing_data = load_json(filename)  # 기존 데이터 로드
    existing_data.extend(new_data)  # 새 데이터 추가
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)
    print(f"✅ JSON 파일 업데이트 완료: {filename} (총 {len(existing_data)}개)")

def scroll_down_with_check(driver, scroll_container, max_scrolls=100):
    last_count = 0
    scroll_attempts = 0
    
    while scroll_attempts < max_scrolls:
        try:
            listings = driver.find_elements(By.CLASS_NAME, "item_link")
            current_count = len(listings)

            if current_count > last_count:  # ✅ 새로운 매물이 로드되었는지 확인
                print(f"🔽 스크롤 {scroll_attempts+1}/{max_scrolls}: {current_count}개 매물 로드됨")
                last_count = current_count
                scroll_attempts += 1
                driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scroll_container)
                time.sleep(random.uniform(3, 5))  # ✅ 랜덤 딜레이
            else:
                print("🚨 더 이상 로드할 매물이 없음")
                break
        except Exception as e:
            print(f"🚨 스크롤 오류 발생: {e}")
            break

def extract_main_photo_url():
    """상세 정보 페이지 내 메인 사진 URL 추출"""
    try:
        main_photo_button = driver.find_element(By.CLASS_NAME, "main_photo_item")
        style_attribute = main_photo_button.get_attribute("style")
        match = re.search(r'url\("([^"]+)"\)', style_attribute)  # `url("...")` 패턴에서 URL 추출
        if match:
            return match.group(1)
        return ""
    except:
        return None

# ✅ 크롤링할 지역 리스트 (JSON 파일 로드)
locations = load_json("seoul_locations.json")

# ✅ 데이터 저장 리스트
JSON_FILENAME = "dongjakgu.json"

def get_random_user_agent():
    """랜덤 User-Agent 반환"""
    return random.choice(user_agents)

for location in locations:
    if location['법정동명'][:9] != "서울특별시 동작구":
        continue
    print(f"📌 크롤링 중: {location['법정동명']}")

    # ✅ 매 요청마다 랜덤 User-Agent 적용
    options.add_argument(f"user-agent={get_random_user_agent()}")
    driver = webdriver.Chrome(service=service, options=options)

    # ✅ 해당 법정동 코드로 검색된 네이버 부동산 페이지 접속
    url = f"https://new.land.naver.com/houses?cortarNo={location['법정동코드']}"
    driver.get(url)
    

    for attempt in range(3):  # 🚨 최대 3번 시도 (새로고침 포함)
        try:
            scroll_container = driver.find_element(By.CLASS_NAME, "item_list--article")
            break  # ✅ 스크롤 컨테이너를 찾았으면 루프 종료
        except:
            print(f"🚨 스크롤 컨테이너를 찾을 수 없음, {attempt+1}번째 시도 후 새로고침")
            driver.refresh()
            time.sleep(random.uniform(3, 6))

    scroll_down_with_check(driver, scroll_container)

    # ✅ 매물 리스트 가져오기
    listings = driver.find_elements(By.CLASS_NAME, "item_link")
    print(f"✅ 총 {len(listings)}개의 매물 발견")

    if not listings:
        print(f"🚨 {location['법정동명']} - 매물 없음")
        driver.quit()
        continue

    all_data = []  # ✅ 동별 데이터 저장
    i = 0

    for listing in listings:
        try:
            i += 1
            listing.click()
            time.sleep(random.uniform(3, 5))  # ✅ 랜덤 딜레이

                #  새로 열린 탭이 있다면 자동으로 닫기
            if len(driver.window_handles) > 1:
                print("🚨 새 탭이 감지됨! 불필요한 탭을 닫습니다.")
                main_window = driver.window_handles[0]  # 원래 창
                for handle in driver.window_handles[1:]:  # 새 탭들
                    driver.switch_to.window(handle)
                    driver.close()
                driver.switch_to.window(main_window)  # 다시 원래 창으로 이동

            current_url = driver.current_url
            match = re.search(r"articleNo=(\d+)", current_url)
            if not match:
                print("🚨 매물 번호(articleNo) 추출 실패")
                continue

            article_no = match.group(1)
            detail_url = f"https://new.land.naver.com/houses?articleNo={article_no}"

            def get_text(xpath):
                try:
                    return driver.find_element(By.XPATH, xpath).text.strip()
                except:
                    return ""

            data = {
                "매물번호": article_no,
                "매물유형" : driver.execute_script("return document.querySelector('.label--category')?.innerText || '';"),
                "거래유형": get_text("//div[contains(@class, 'info_article_price')]/span[1]"),
                "가격": get_text("//div[contains(@class, 'info_article_price')]//span[contains(@class, 'price')]"),
                "소재지": get_text("//th[contains(text(), '소재지')]/following-sibling::td"),
                "매물특징": get_text("//th[contains(text(), '매물특징')]/following-sibling::td"),
                "공급/전용면적": get_text("//th[contains(text(), '공급/전용면적')]/following-sibling::td"),
                "해당층/총층": get_text("//th[contains(text(), '해당층/총층')]/following-sibling::td"),
                "방수/욕실수": get_text("//th[contains(text(), '방수/욕실수')]/following-sibling::td"),
                "관리비": get_text("//th[contains(text(), '관리비')]/following-sibling::td"),
                "입주 가능일": get_text("//th[contains(text(), '입주가능일')]/following-sibling::td"),
                "방향": get_text("//th[contains(text(), '방향')]/following-sibling::td"),
                "URL": detail_url,
                "메인사진": extract_main_photo_url()
            }

            all_data.append(data)
            print(f"✅ 상세 정보 수집 완료: {data['소재지']} - {data['가격']}, {i}/{len(listings)}")
            time.sleep(random.uniform(2, 4))  
        

        except Exception as e:            
            print(f"🚨 상세 페이지 이동 오류: {e}")
            print(f"🚨 {location['법정동명']} 크롤링 중단, 다음 동으로 이동")
            break  # ✅ 해당 동 크롤링 중단하고 다음 동으로 이동

    # ✅ 동별로 JSON 파일 저장
    if all_data:
        save_data_to_json(JSON_FILENAME, all_data)

    print(f"📌 {location['법정동명']} 크롤링 완료!")

    driver.get(url)
    time.sleep(random.uniform(5, 10))  # ✅ 랜덤 딜레이
    driver.quit()