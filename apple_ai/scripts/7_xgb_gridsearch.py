# scripts/7_xgb_gridsearch.py
# 가장 최적의 방법을 찾아서 가중치

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import make_scorer, r2_score
from xgboost import XGBRegressor
from math import sqrt

# 데이터 불러오기
df = pd.read_csv('features/apple_features.csv')
X = df.drop(columns=['filename', 'grade', 'SSC'])
y = df['SSC']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# RMSE 계산용 스코어러 생성
def rmse(y_true, y_pred):
    from sklearn.metrics import mean_squared_error
    return sqrt(mean_squared_error(y_true, y_pred))

rmse_scorer = make_scorer(rmse, greater_is_better=False)

# 파라미터 그리드 정의
param_grid = {
    'n_estimators': [100, 300],
    'max_depth': [4, 6, 8],
    'learning_rate': [0.05, 0.1],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

# GridSearchCV 수행
xgb = XGBRegressor(random_state=42)
grid_search = GridSearchCV(estimator=xgb,
                           param_grid=param_grid,
                           scoring=rmse_scorer,
                           cv=3,
                           verbose=1,
                           n_jobs=-1)

print("\n🔍 XGBoost Grid Search 시작 중...")
grid_search.fit(X_train, y_train)

# 최적 파라미터 및 성능 출력
best_model = grid_search.best_estimator_
best_params = grid_search.best_params_
y_pred = best_model.predict(X_test)

from sklearn.metrics import r2_score, mean_squared_error
r2 = r2_score(y_test, y_pred)
rmse_val = sqrt(mean_squared_error(y_test, y_pred))

print("\n✅ 최적 파라미터:")
print(best_params)
print(f"\n📈 R^2 Score: {r2:.4f}")
print(f"📉 RMSE: {rmse_val:.4f}")
