# scripts/predict_from_image.py (다중 이미지 예측용)

import os
import cv2
import numpy as np
import joblib
import pandas as pd
from skimage.feature import graycomatrix, graycoprops
from skimage.color import deltaE_cie76

# 설정
MODEL_PATH = 'models/ssc_xgb_model.pkl'
LAB_REFERENCE = np.array([60, 150, 140])
IMAGE_DIR = 'crops/samples'  # 예측할 이미지 폴더 경로

# 모델 불러오기
model = joblib.load(MODEL_PATH)

def extract_features(image):
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

# 전체 이미지 폴더에서 반복 예측
data = []
for file in os.listdir(IMAGE_DIR):
    if not file.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue
    path = os.path.join(IMAGE_DIR, file)
    img = cv2.imread(path)
    if img is None:
        print(f"❌ 이미지 불러오기 실패: {file}")
        continue
    try:
        features = extract_features(img)
        X = pd.DataFrame([features])
        pred = model.predict(X)[0]
        print(f"🍎 {file}: {pred:.2f} °Brix")
        features['filename'] = file
        features['predicted_ssc'] = round(pred, 2)
        data.append(features)
    except Exception as e:
        print(f"❌ 처리 실패: {file} → {e}")

# 전체 결과 저장
if data:
    df = pd.DataFrame(data)
    df.to_csv('features/sample_predictions.csv', index=False)
    print("\n✅ 전체 예측 완료! 결과 저장: features/sample_predictions.csv")
