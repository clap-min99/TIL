# scripts/1_crop_and_extract.py

import os
import json
import cv2
import numpy as np
import pandas as pd
from skimage.feature import graycomatrix, graycoprops
from skimage.color import deltaE_cie76
from math import ceil
preview_images = []

# 기본 경로 설정
IMG_DIR = 'data/images'
JSON_DIR = 'data/json'
CROP_DIR = 'crops'
FEATURE_PATH = 'features/apple_features_image.csv'
os.makedirs(CROP_DIR, exist_ok=True)
os.makedirs('features', exist_ok=True)

# 기준 Lab 값 (ΔE 계산용)
LAB_REFERENCE = np.array([60, 150, 140])

def apply_clahe(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    L, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    L_clahe = clahe.apply(L)

    lab_clahe = cv2.merge((L_clahe, a, b))
    corrected = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)
    return corrected


# Feature 추출 함수
def extract_features(image):
    image = apply_clahe(image)
    img_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    L, a, b = cv2.split(img_lab)
    H, S, V = cv2.split(img_hsv)

    L_mean = np.mean(L)
    a_mean = np.mean(a)
    b_mean = np.mean(b)
    H_mean = np.mean(H)
    S_mean = np.mean(S)
    V_mean = np.mean(V)

    a_div_b = a_mean / (b_mean + 1e-5)
    a_div_L = a_mean / (L_mean + 1e-5)
    delta_e = deltaE_cie76([[L_mean, a_mean, b_mean]], [LAB_REFERENCE])[0]

    glcm = graycomatrix(gray, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)
    contrast = graycoprops(glcm, 'contrast')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
    correlation = graycoprops(glcm, 'correlation')[0, 0]

    thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)[1]
    x, y, w, h = cv2.boundingRect(thresh)
    area = cv2.countNonZero(thresh)
    aspect_ratio = w / (h + 1e-5)

    return {
        'L_mean': L_mean,
        'a_mean': a_mean,
        'b_mean': b_mean,
        'H_mean': H_mean,
        'S_mean': S_mean,
        'V_mean': V_mean,
        'a_div_b': a_div_b,
        'a_div_L': a_div_L,
        'delta_E': delta_e,
        'contrast': contrast,
        'energy': energy,
        'homogeneity': homogeneity,
        'correlation': correlation,
        'area': area,
        'aspect_ratio': aspect_ratio,
    }

# 전체 수행
data = []

for filename in os.listdir(JSON_DIR):
    if filename.endswith('.json'):
        json_path = os.path.join(JSON_DIR, filename)        
        try:
            with open(json_path, 'r', encoding='utf-8-sig') as f:
                meta = json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError) as e1:
            try:
                with open(json_path, 'r', encoding='cp949') as f:
                    meta = json.load(f)
            except Exception as e2:
                print(f"❌ JSON 불러오기 실패: {filename} → {e2}")
                continue

        img_name = meta['images']['img_file_name']
        img_path = os.path.join(IMG_DIR, img_name)
        if not os.path.exists(img_path):
            print(f"❌ 이미지 없음: {img_name}")
            continue

        # crop용 마스크 생성
        points = np.array(meta['annotations']['segmentation']).reshape(-1, 2).astype(np.int32)
        original = cv2.imread(img_path)
        mask = np.zeros(original.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [points], 255)

        masked = cv2.bitwise_and(original, original, mask=mask)
        x, y, w, h = cv2.boundingRect(mask)
        crop = masked[y:y+h, x:x+w]

        # 저장
        crop_name = os.path.splitext(img_name)[0] + '_crop.jpg'
        crop_path = os.path.join(CROP_DIR, crop_name)
        cv2.imwrite(crop_path, crop)

        try:
            features = extract_features(crop)
            features['filename'] = crop_name
            features['SSC'] = meta['collection']['sugar_content_nir']
            features['grade'] = meta['annotations']['sugar_grade']
            data.append(features)
            print(f"✅ 처리 완료: {crop_name}")
        except Exception as e:
            print(f"❌ {crop_name} 추출 실패: {e}")

# 저장
df = pd.DataFrame(data)
df.to_csv(FEATURE_PATH, index=False)
print(f"\n✅ 전체 완료! 추출된 특징 CSV 저장: {FEATURE_PATH}")
