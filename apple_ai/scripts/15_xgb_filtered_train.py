# scripts/15_xgb_filtered_train.py
# 중요한 feature 기반으로 학습했을 때 결과

import pandas as pd
import joblib
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt

# 유지할 주요 feature만 선정 (SHAP 기반)
selected_features = [
    'a_mean', 'area', 'b_mean', 'homogeneity',
    'energy', 'S_mean'  # 영향력 높고 방향성 뚜렷했던 feature들
]

# 데이터 로드 및 필터링
df = pd.read_csv('features/apple_features.csv')
X = df[selected_features]
y = df['SSC']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model = XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# 예측 및 평가
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = sqrt(mean_squared_error(y_test, y_pred))

print("\n✅ 중요 feature 기반 XGBoost 재학습 완료")
print(f"R^2 Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# 모델 저장
joblib.dump(model, 'models/ssc_xgb_filtered.pkl')
print("\n📦 모델 저장 완료: models/ssc_xgb_filtered.pkl")
