# scripts/5_feature_importance_and_retrain.py
# 모델 만들때 가장 영향이 높은 요인들 찾는 코드

import joblib
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from xgboost import XGBRegressor

# 모델 및 데이터 로딩
model = joblib.load('models/ssc_xgb_model.pkl')
df = pd.read_csv('features/apple_features.csv')

# 입력 X, 라벨 y 분리
X = df.drop(columns=['filename', 'grade', 'SSC'])
y = df['SSC']

# 1. Feature 중요도 계산
importances = model.feature_importances_
features = X.columns
importance_df = pd.DataFrame({'feature': features, 'importance': importances})
importance_df = importance_df.sort_values(by='importance', ascending=False)

# 2. 상위 N개 feature 선택 (예: 8개)
TOP_N = 5
top_features = importance_df.head(TOP_N)['feature'].tolist()
print(f"\n🎯 상위 {TOP_N}개 feature: {top_features}")

# 3. 선택된 feature만으로 재학습
X_top = X[top_features]
X_train, X_test, y_train, y_test = train_test_split(X_top, y, test_size=0.2, random_state=42)

model_top = XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
model_top.fit(X_train, y_train)

# 4. 성능 평가
y_pred = model_top.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = sqrt(mean_squared_error(y_test, y_pred))

print(f"\n📈 재학습 성능")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# 5. 시각화
importance_df.head(10).plot(kind='barh', x='feature', y='importance', legend=False)
plt.title("XGBoost Feature Importance (Top 10)")
plt.xlabel("Importance")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# 6. 모델 저장 (선택)
joblib.dump(model_top, 'models/ssc_xgb_model_top8.pkl')
print("\n✅ 중요 feature 기반 모델 저장 완료: models/ssc_xgb_model_top8.pkl")
