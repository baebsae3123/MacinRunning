import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import joblib

# 데이터 불러오기
data = pd.read_json("EDUM.json")

# 문자열 → 숫자 변환
encoder = LabelEncoder()
data["product_used"] = encoder.fit_transform(data["product_used"])

# 입력 데이터
X = data[[
"sebum_level",
"skin_irritation",
"sleep_hours",
"oily_food",
"water_intake_ml",
"product_used"
]]

# 출력 데이터
y = data["acne_count"]

# 학습 / 테스트 분리
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

# 모델 생성
model = RandomForestRegressor()

# 학습
model.fit(X_train, y_train)

# 예측
pred = model.predict(X_test)

# 성능 평가
mse = mean_squared_error(y_test, pred)
r2 = r2_score(y_test, pred)

print("예측 여드름 개수:", mse)
print("여드름 발생 확률:", r2)

# 모델 저장
joblib.dump(model, "model.pkl")

print("모델 저장 완료")