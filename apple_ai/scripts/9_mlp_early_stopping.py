# scripts/10_mlp_early_stopping.py

import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
from torch.utils.data import TensorDataset, DataLoader
from math import sqrt

# 데이터 로딩 및 전처리
df = pd.read_csv('features/apple_features.csv')
X = df.drop(columns=['filename', 'grade', 'SSC']).values
y = df['SSC'].values.reshape(-1, 1)

scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)

train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# MLP 모델 정의
class MLPRegressor(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )

    def forward(self, x):
        return self.model(x)

# 모델, 손실 함수, 옵티마이저 초기화
model = MLPRegressor(X.shape[1])
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# EarlyStopping 설정
patience = 10
best_loss = float('inf')
best_model_state = None
wait = 0

train_losses = []

# 학습 루프
epochs = 100
for epoch in range(epochs):
    model.train()
    epoch_loss = 0.0
    for xb, yb in train_loader:
        pred = model(xb)
        loss = criterion(pred, yb)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()

    avg_loss = epoch_loss / len(train_loader)
    train_losses.append(avg_loss)
    print(f"Epoch {epoch+1}, Loss: {avg_loss:.4f}")

    if avg_loss < best_loss:
        best_loss = avg_loss
        best_model_state = model.state_dict()
        wait = 0
    else:
        wait += 1
        if wait >= patience:
            print(f"\n⏹ EarlyStopping triggered at epoch {epoch+1} (best loss: {best_loss:.4f})")
            break

# 최적 모델 복원 및 평가
model.load_state_dict(best_model_state)
model.eval()
y_pred_scaled = model(X_test).detach().numpy()
y_pred = scaler_y.inverse_transform(y_pred_scaled)
y_true = scaler_y.inverse_transform(y_test)

r2 = r2_score(y_true, y_pred)
rmse = sqrt(mean_squared_error(y_true, y_pred))
print(f"\n📈 R^2 Score: {r2:.4f}")
print(f"📉 RMSE: {rmse:.4f}")

# 손실 시각화
plt.plot(train_losses)
plt.xlabel('Epoch')
plt.ylabel('Training Loss (MSE)')
plt.title('Training Loss over Epochs')
plt.grid(True)
plt.tight_layout()
plt.savefig('features/mlp_loss_curve.png')
print("\n📊 학습 손실 시각화 저장 완료: features/mlp_loss_curve.png")
