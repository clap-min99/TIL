# scripts/9_lightgbm_top_features.py
# LightGBM 모델
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from lightgbm import LGBMRegressor
from math import sqrt

# 데이터 로드 및 상위 feature 선택
df = pd.read_csv('features/apple_features.csv')
top_features = ['correlation', 'contrast', 'aspect_ratio', 'a_div_b', 'homogeneity']
X = df[top_features]
y = df['SSC']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# LightGBM 모델 학습
model = LGBMRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# 예측 및 평가
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = sqrt(mean_squared_error(y_test, y_pred))

print("\n✅ LightGBM 모델 평가 (상위 feature 기반)")
print(f"R^2 Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# 모델 저장
import joblib
joblib.dump(model, 'models/ssc_lgbm_top.pkl')
print("\n📦 모델 저장 완료: models/ssc_lgbm_top.pkl")
