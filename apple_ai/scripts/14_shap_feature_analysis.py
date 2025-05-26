# scripts/14_shap_feature_analysis.py

import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# 모델 및 데이터 로드
model = joblib.load('models/ssc_xgb_model.pkl')
df = pd.read_csv('features/apple_features.csv')
X = df.drop(columns=['filename', 'grade', 'SSC'])
y = df['SSC']

# SHAP 분석 객체 생성
explainer = shap.Explainer(model)
shap_values = explainer(X)

# SHAP summary plot 저장
plt.figure(figsize=(10, 6))
shap.summary_plot(shap_values, X, show=False)
plt.tight_layout()
plt.savefig('features/shap_summary.png')
print("\n📊 SHAP summary plot 저장 완료: features/shap_summary.png")
