# MacinRunning
2학년1학기 머신러닝 - 여드름 피부 상태 피드백 프로젝트

# 프로젝트 참가 1명
황인성 

## 발표
[![Design 보기](https://img.shields.io/badge/🎨%20Design%20View-MiriCanvas-FF6F61?style=for-the-badge)](https://www.miricanvas.com/login?redirect=%2Fv2%2Fko%2Fdesign2%2F996aaac8-050c-41c2-80b8-fb92c7168b3f%3Flocation%3Ddesign%26type%3Dcopy_link%26access%3Dlink%26permission%3Dviewer)

## 목표: 여드름 피부 상태가 매일 달라서 뭐 써야할지에 대해 

# 백엔드

데이터 가져오는곳 : https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset?resource=download

서버: http://127.0.0.1:5000/

| 번호 | 사용 모델                 |
| -- | --------------------- |
| 1  | RandomForestRegressor |
| 2  |                       |
| 3  |                       |
| 4  |                       |
| 5  |                       |
| 6  |                       |
| 7  |                       |
| 8  |                       |



학습방법 : 지도 학습식

모델명: model.pkl / 데이터 Sleep_health_and_lifestyle_dataset.csv

# 작동원리

수면 많으면 건강 ↑

스트레스 높으면 건강 ↓

활동 많으면 건강 ↑

데이터

| 컬럼              | 의미          |
| --------------- | ----------- |
| Acne_Count      | 여드름 개수      |
| Sebum_Level     | 피지량 (1~3)   |
| Skin_Irritation | 피부 자극 (1~3) |
| Sleep_Hours     | 수면시간        |
| Oily_Food       | 기름진 음식 먹었는지 |
| Water_Intake_ml | 물 섭취량       |
등을 받아 예상하여 결과를 추측함 

# 사용 언어 + 프로그램
## 💻Frontend
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
## Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
## 배포 환경
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
## 개발 환경
![VS Code](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
## Database
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
## 핵심기능
🧠 건강 점수
🌿 피부 점수
📊 분석 결과
🧴 추천 화장품

건강 점수 계산 / 피부 점수 계산 / 분석결과 / 추천 화장품 
## API 구조
아직 모름

# 머신러닝
머신러닝은 컴퓨터가 데이터로부터 스스로 학습하는 기술이다.
사람이 규칙을 직접 만드는 대신 데이터 패턴을 찾아 예측한다


# 2주제 발표

## 모델선택이유
 RandomForestRegressor / XGBRegressor / KMeans  등을 선택했는데
 
 🔹 RandomForestRegressor
다양한 "환자" 특징을 고려한 안정적인 예측 성능 확보 를 위해
과적합을 줄이고 기본 성능 비교 기준 모델로 활용

🔹 XGBRegressor
Gradient Boosting 기반으로 높은 예측 정확도 기대
RandomForest와 비교하여 성능 개선 여부 분석

🔹 K-Means Clustering
비지도 학습을 통해 데이터의 잠재적 구조 파악
유사한 특성을 가진 데이터 간 군집 형성 및 패턴 분석


## 성능비교
모델별결과를지표로비교분석

| 순위 | 모델               | MSE (낮을수록 좋음) | R² (높을수록 좋음) | 평가          |
| -- | ---------------- | ------------- | ------------ | ----------- |
| 🥇 | XGBoost          | 0.003         | 0.998        | 가장 정확       |
| 🥈 | RandomForest     | 0.008         | 0.995        | 안정적, 높은 성능  |
| 🥉 | LinearRegression | 0.133         | 0.912        | 기본 모델 대비 양호 |
| ❌  | SVR              | 1.162         | 0.23         | 성능 낮음       |


## 결과해석
어떤모델이왜더좋은가

<img width="743" height="466" alt="image" src="https://github.com/user-attachments/assets/dce7a8d4-5cda-4ce1-b379-15f47c30520a" />

<img width="700" height="435" alt="image" src="https://github.com/user-attachments/assets/52397d96-061e-4713-b623-d4014ea764d9" />


# 실행방법
pyrhon app.py
