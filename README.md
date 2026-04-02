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

# 📊 모델별 선택 이유

중요하게 4가지만 뽑음 ★★★
🔹 LinearRegression 
변수 간 기본적인 선형 관계를 확인하기 위해 사용 

다른 모델과 비교하기 위한 기준(Baseline) 모델

데이터의 기본적인 선형 관계를 파악하고, 성능 비교 기준으로 활용하기 위해 선택하였다.

(데이터를 선형관계 연결함으로써 더 좋은 정확도가 나올거라 예상함)

🔹 RandomForestRegressor 
여러 트리를 활용하여 안정적인 예측 성능 확보

과적합을 줄이고 일반화 성능이 우수

앙상블 기법을 통해 안정적이고 신뢰성 있는 예측 성능을 확보하기 위해 선택하였다.

양상블 기법이란 : 앙상블 기법은 여러 개의 모델을 결합하여 단일 모델보다 더 높은 예측 성능과 안정성을 확보하는 방법이다.

( 다양한 데이터들이 많으니 여러 트리가 많은 모델이 좋다고 생각함)

🔹 XGBRegressor (XGBoost)
Gradient Boosting 기반으로 높은 예측 정확도 기대

복잡한 데이터 패턴을 효과적으로 학습

Boosting 기법을 활용하여 높은 예측 성능과 복잡한 패턴 학습을 위해 선택하였다.

Boosting기법 이란 : Boosting은 이전 모델의 예측 오차를 반복적으로 보완하며 학습하는 방식으로, 점진적으로 성능을 향상시키는 알고리즘이다.

 (데이터들이 정말많고 데이터들이 복잡하게 있으며 패턴을 효과적으로 학습기에 좋은 모델이라 선택함)

🔹 SVR (Support Vector Regression) 
커널 함수를 활용하여 비선형 데이터 학습 가능

커널 함수란 : 커널 함수는 데이터를 고차원 공간으로 변환하여 선형적으로 분리하기 어려운 비선형 패턴을 효과적으로 학습할 수 있도록 하는 기법이다.

( 비선형 데이터의 복잡한 패턴을 분석할수있어 다양한 데이터에 유연하게 대응할수있어서 좋은모델이라 선택함) 


다른 방식의 모델과 성능 비교 목적
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

👉 데이터가 복잡한 패턴(비선형)이라서

수면시간 + 스트레스 + 활동량등을 학습해야하기 떄문에
XGBoost와 RandomForest는 비선형 관계를 효과적으로 학습하여 높은 성능을 보였으며,
특히 XGBoost가 가장 좋은 성적을 보여줌
반면, LinearRegression은 상대적으로 단순한 모델 구조로 인해 성능이 다소 낮았고,
SVR은 데이터 특성과 맞지 않아 낮은 성능을 보였다.

| 구분     | RandomForest                   | XGBoost                             |
| ------ | ------------------------------ | ----------------------------------- |
| 학습 방식  | 여러 트리를 독립적으로 생성 후 평균 (Bagging) | 이전 모델의 오차를 보완하며 순차적으로 학습 (Boosting) |
| 특징     | 안정적이고 과적합에 강함                  | 높은 정확도, 정밀한 예측                      |
| 오차 처리  | 전체 평균으로 완화                     | 틀린 부분을 집중적으로 수정                     |
| 데이터 학습 | 전체적인 패턴 학습                     | 세밀한 패턴까지 학습                         |
| 성능 결과  | MSE: 0.008 / R²: 0.995         | MSE: 0.003 / R²: 0.998              |
| 장점     | 구현 간단, 안정성 높음                  | 높은 성능, 복잡한 데이터에 강함                  |
| 단점     | 세밀한 예측 한계                      | 튜닝 필요, 계산 비용 높음                     |

## 개인적으로 XGBoost가 더 좋은 성능이 나온이유는 틀린 부분을 더 집중적으로 수정하기떄문에 더 좋은 성능의 모델이 되지않았을까 생각합나다.

<img width="743" height="466" alt="image" src="https://github.com/user-attachments/assets/dce7a8d4-5cda-4ce1-b379-15f47c30520a" />

<img width="700" height="435" alt="image" src="https://github.com/user-attachments/assets/52397d96-061e-4713-b623-d4014ea764d9" />


# 실행방법
pyrhon app.py
