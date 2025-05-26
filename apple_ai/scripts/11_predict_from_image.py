# scripts/11_predict_from_image.py

import cv2
import numpy as np
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
from features.extractor import extract_features  # 🟡 모듈 분리되어 있다고 가정

# 모델 및 스케일러 로드
model = joblib.load('models/ssc_lgbm_top.pkl')
df = pd.read_csv('features/apple_features.csv')
top_features = ['correlation', 'contrast', 'aspect_ratio', 'a_div_b', 'homogeneity']
scaler = StandardScaler()
scaler.fit(df[top_features])


# 이미지 → Brix 예측 함수
def predict_brix_from_image(img_path):
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"이미지를 불러올 수 없습니다: {img_path}")

    features = extract_features(img)
    X_input = np.array([[features[f] for f in top_features]])
    X_scaled = scaler.transform(X_input)

    y_pred = model.predict(X_scaled)[0]
    return round(float(y_pred), 2)

# 예시 테스트
if __name__ == '__main__':
    test_img_path = 'data/sample.png'  # 예시용 이미지 경로
    try:
        result = predict_brix_from_image(test_img_path)
        print(f"\n🍎 예측된 사과 당도 (SSC): {result} °Brix")
    except Exception as e:
        print(f"\n❌ 예측 실패: {e}")
