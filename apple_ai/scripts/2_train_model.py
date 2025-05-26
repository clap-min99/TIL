# XGBoost로 학습
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
from xgboost import XGBRegressor
import joblib
import os

# 경로 설정
DATA_PATH = 'features/apple_features.csv'
MODEL_PATH = 'models/ssc_xgb_model.pkl'
os.makedirs('models', exist_ok=True)

# 데이터 로드
df = pd.read_csv(DATA_PATH)

# X (입력 특징), y (SSC 값) 분리
X = df.drop(columns=['filename', 'grade', 'SSC'])
y = df['SSC']

# 학습/테스트 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 정의 및 학습
model = XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# 예측 및 평가
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = sqrt(mean_squared_error(y_test, y_pred))

print(f"✅ R² Score: {r2:.4f}")
print(f"✅ RMSE: {rmse:.4f}")

# 모델 저장
joblib.dump(model, MODEL_PATH)
print(f"✅ 모델 저장 완료: {MODEL_PATH}")
