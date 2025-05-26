# scripts/13_evaluate_within_range.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import joblib
import numpy as np
from math import sqrt

# 모델 및 데이터 로드
model = joblib.load('models/ssc_xgb_model.pkl')
df = pd.read_csv('features/apple_features.csv')

X = df.drop(columns=['filename', 'grade', 'SSC'])
y = df['SSC'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y_pred = model.predict(X_test)

# 오차 범위 내 정확도 계산 함수
def accuracy_within_range(y_true, y_pred, delta):
    return np.mean(np.abs(y_true - y_pred) <= delta)

# 지표 계산
r2 = r2_score(y_test, y_pred)
rmse = sqrt(mean_squared_error(y_test, y_pred))
acc_0_3 = accuracy_within_range(y_test, y_pred, 0.3)
acc_0_5 = accuracy_within_range(y_test, y_pred, 0.5)
acc_1_0 = accuracy_within_range(y_test, y_pred, 1.0)

# 결과 출력
print(f"\n📈 R^2 Score: {r2:.4f}")
print(f"📉 RMSE: {rmse:.4f}")
print(f"\n✅ Accuracy@0.3: {acc_0_3:.2%}")
print(f"✅ Accuracy@0.5: {acc_0_5:.2%}")
print(f"✅ Accuracy@1.0: {acc_1_0:.2%}")
