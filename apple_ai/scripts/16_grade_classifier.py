# scripts/16_grade_classifier.py

import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# 당도 → 등급 변환 함수
def to_grade(ssc):
    if ssc >= 14.5:
        return 'A'
    elif ssc >= 13.5:
        return 'B'
    else:
        return 'C'

# 데이터 불러오기 및 등급 라벨 추가
df = pd.read_csv('features/apple_features.csv')
df['grade_label'] = df['SSC'].apply(to_grade)

# 문자열 등급 → 숫자 인코딩
le = LabelEncoder()
y_encoded = le.fit_transform(df['grade_label'])

X = df.drop(columns=['filename', 'grade', 'SSC', 'grade_label'])
y = y_encoded

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 분류 모델 학습
model = XGBClassifier(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# 예측 및 평가
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n✅ 등급 분류 정확도: {acc:.2%}")
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Confusion matrix 시각화
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=le.classes_, yticklabels=le.classes_)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.savefig('features/classifier_confusion_matrix.png')
print("\n📊 Confusion matrix 저장 완료: features/classifier_confusion_matrix.png")

# 모델 저장
joblib.dump(model, 'models/ssc_xgb_classifier.pkl')
print("\n📦 분류 모델 저장 완료: models/ssc_xgb_classifier.pkl")
