from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# 모델 로드
model = joblib.load("model.pkl")

# CSV 데이터 로드
data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# BMI 변환
bmi_map = {
    "Underweight": 0,
    "Normal": 1,
    "Overweight": 2,
    "Obese": 3
}

# 화장품 DB
products_db = {
    "oily": [
        "COSRX Salicylic Acid Cleanser",
        "La Roche-Posay Effaclar Gel",
        "Innisfree Volcanic Pore Clay Mask"
    ],
    "sensitive": [
        "Etude SoonJung 2x Barrier Cream",
        "Dr.G Green Mild Up Sun",
        "La Roche-Posay Cicaplast Baume"
    ],
    "normal": [
        "Laneige Cream Skin Refiner",
        "Innisfree Green Tea Seed Serum",
        "COSRX Advanced Snail 96 Essence"
    ]
}

# -------------------------
# 화장품 추천 (나이 포함)
# -------------------------
def recommend_products(stress, sleep, age):

    if stress >= 7:
        return products_db["sensitive"]

    elif sleep <= 5:
        return products_db["oily"]

    elif age >= 35:
        return [
            "Laneige Cream Skin Refiner",
            "Innisfree Green Tea Seed Serum",
            "COSRX Advanced Snail 96 Essence"
        ]

    else:
        return products_db["normal"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data_json = request.get_json()
        print("받은 데이터:", data_json)

        # -------------------------
        # 입력값
        # -------------------------
        age = float(data_json.get("age", 25))
        sleep = float(data_json.get("sleep_duration", 7))
        stress = float(data_json.get("stress_level", 5))
        activity = float(data_json.get("activity", 5))
        heart = float(data_json.get("heart_rate", 70))
        steps = float(data_json.get("daily_steps", 5000))

        bmi_text = data_json.get("bmi", "Normal")
        bmi = bmi_map.get(bmi_text, 1)

        # -------------------------
        # AI 입력 (기존 모델 유지)
        # -------------------------
        input_data = np.array([[
            sleep,
            stress,
            activity,
            heart,
            steps / 10000,
            bmi
        ]])

        print("모델 입력:", input_data)

        # AI 예측
        prediction = model.predict(input_data)
        ai_score = float(prediction[0])

        if ai_score <= 1:
            ai_score *= 100

        # -------------------------
        # 규칙 기반 건강 점수
        # -------------------------
        health_score = 50

        # 수면
        if sleep >= 7:
            health_score += 15
        elif sleep >= 6:
            health_score += 5
        else:
            health_score -= 10

        # 스트레스
        health_score -= stress * 2

        # 활동
        health_score += activity * 2

        # 심박수
        if 60 <= heart <= 80:
            health_score += 10
        else:
            health_score -= 5

        # 걸음수
        if steps >= 8000:
            health_score += 15
        elif steps >= 5000:
            health_score += 5
        else:
            health_score -= 10

        # BMI
        if bmi == 1:
            health_score += 10
        else:
            health_score -= 5

        # 🔥 나이 보정
        if age < 25:
            health_score += 5
        elif age < 40:
            health_score += 0
        else:
            health_score -= 5

        # 최종 점수
        final_score = (health_score + ai_score) / 2
        final_score = max(0, min(100, final_score))

        # -------------------------
        # 피부 점수 (나이 포함)
        # -------------------------
        skin_score = 100 - (stress * 6) + (sleep * 3) - (age * 0.3)
        skin_score = max(0, min(100, skin_score))

        # -------------------------
        # 화장품 추천
        # -------------------------
        products = recommend_products(stress, sleep, age)

        # -------------------------
        # 위험 경고 (추가 기능🔥)
        # -------------------------
        warning = None

        if age > 40 and steps < 4000:
            warning = "운동 부족 위험"

        if sleep < 5:
            warning = "수면 부족 위험"

        return jsonify({
            "health_score": round(final_score),
            "skin_score": round(skin_score),
            "products": products,
            "warning": warning
        })

    except Exception as e:
        print("에러:", e)

        return jsonify({
            "health_score": 0,
            "skin_score": 0,
            "products": [],
            "error": str(e)
        })


@app.route("/data")
def get_data():
    return data.to_json(orient="records")


if __name__ == "__main__":
    app.run(debug=True)