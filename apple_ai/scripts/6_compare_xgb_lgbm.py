# scripts/6_compare_xgb_lgbm.py
# XGBoost랑 Lightgbm 성능 테스트

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from math import sqrt

# 데이터 로드
df = pd.read_csv('features/apple_features.csv')
X = df.drop(columns=['filename', 'grade', 'SSC'])
y = df['SSC']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# XGBoost 학습
xgb_model = XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)
r2_xgb = r2_score(y_test, y_pred_xgb)
rmse_xgb = sqrt(mean_squared_error(y_test, y_pred_xgb))

# LightGBM 학습
lgbm_model = LGBMRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
lgbm_model.fit(X_train, y_train)
y_pred_lgbm = lgbm_model.predict(X_test)
r2_lgbm = r2_score(y_test, y_pred_lgbm)
rmse_lgbm = sqrt(mean_squared_error(y_test, y_pred_lgbm))

# 결과 출력
print("\n✅ XGBoost 성능")
print(f"R²: {r2_xgb:.4f} | RMSE: {rmse_xgb:.4f}")

print("\n✅ LightGBM 성능")
print(f"R²: {r2_lgbm:.4f} | RMSE: {rmse_lgbm:.4f}")
