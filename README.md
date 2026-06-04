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

---

# 1주제 발표

1 문제 정의서
해결할 문제와 예측 목표를 구체적으로 설명

2 데이터 설명
출처 : https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset?resource=download)
크기 : 350개
주요 변수정리 : Acne_Count	여드름 개수 ,Sebum_Level	피지량 (1~3) , Skin_Irritation	피부 자극 (1~3)
Sleep_Hours	수면시간 ,Oily_Food	기름진 음식 먹었는지 ,Water_Intake_ml	물 섭취량


3 기본 모델 실행
첫 번째 ML 모델 실행 결과 제시 : 첫번째 모델 RandomForestRegressor 모델 사용

<img width="743" height="466" alt="image" src="https://github.com/user-attachments/assets/ae6d55ca-d7c8-4f6e-83e9-239c704ca19e" />
다른모델에 비해 성능이 좋지 못함

4 성능 지표 해석
Accuracy, Precision 등 기본 지표 설명
RandomForest	=  Accuracy(0.008) , Precision(0.995)

5 현재 한계 정리
모델의 문제점과 개선 방향 정리
더 정확도 좋은 모델을 써야겠다.

---

# 2주제 발표

# 📊 모델별 선택 이유

중요하게 생각하는 4가지만 뽑음 ★★★

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

# 3주차 반복 수정 기록

## 하이퍼파라미터 조정

learning rate, max depth, regularization 등

| 구분                | 적용 내용               | 코드 예시                                             | 목적              | 기대 효과             |   |
| ----------------- | ------------------- | ------------------------------------------------- | --------------- | ----------------- | - |
| 하이퍼파라미터 조정        | learning_rate 조정    | `"learning_rate": [0.01, 0.05, 0.1]`              | 학습 속도 최적화       | 과적합 감소, 안정적 학습    |   |
| 하이퍼파라미터 조정        | max_depth 조정        | `"max_depth": [3, 4, 5]`                          | 트리 깊이 조절        | 복잡도 조절, 일반화 성능 향상 |   |
| 하이퍼파라미터 조정        | regularization 적용   | `"reg_alpha": [0, 0.1]`<br>`"reg_lambda": [1, 2]` | 과적합 방지          | 노이즈 감소, 모델 안정화    |   |
| 하이퍼파라미터 조정        | n_estimators 조정     | `"n_estimators": [100, 300]`                      | 트리 개수 조절        | 예측 성능 향상          |   |
| 하이퍼파라미터 조정        | SVR 파라미터 조정         | `"C"`, `"gamma"`, `"epsilon"`                     | 오차 허용 범위 조절     | SVR 성능 개선         |   |

---

## 데이터 전처리 변경

feature scaling, feature selection, 데이터 확장

| 구분                | 적용 내용               | 코드 예시                           | 목적              | 기대 효과          |
| ----------------- | ------------------- | ------------------------------- | --------------- | -------------- |
| 데이터 전처리           | Feature Scaling     | `StandardScaler()`              | 변수 크기 통일        | 거리 기반 모델 성능 향상 |
| 데이터 전처리           | 결측치 처리              | `X.fillna(X.mean())`            | 빈 데이터 처리        | 학습 오류 방지       |
| 데이터 전처리           | One-Hot Encoding    | `pd.get_dummies()`              | 범주형 데이터 변환      | 모델 입력 가능       |
| 데이터 전처리           | Blood Pressure 분리   | `"120/80" → 120, 80`            | 문자열 수치화         | 정보 활용도 증가      |
| Feature Selection | 중요 변수 선택            | `SelectKBest()`                 | 중요한 변수만 사용      | 노이즈 감소, 과적합 감소 |
| 데이터 확장            | Stress_per_Sleep 생성 | `Stress Level / Sleep Duration` | 스트레스-수면 관계 반영   | 패턴 학습 강화       |
| 데이터 확장            | Activity_Heart 생성   | `Activity / Heart Rate`         | 활동량 대비 건강 상태 반영 | 건강 패턴 분석 강화    |
| 데이터 확장            | Log_DailySteps 생성   | `np.log1p(Daily Steps)`         | 극단값 완화          | 데이터 안정화        |

---

# 제출물 작성

모델 비교표, 성능 그래프, 변화 원인 분석

## 모델 비교표 

| 모델                | 특징                  | 장점            | 단점            | 예상 성능   |
| ----------------- | ------------------- | ------------- | ------------- | ------- |
| Linear Regression | 선형 관계 기반 예측         | 구조 단순, 해석 쉬움  | 복잡한 패턴 학습 어려움 | 낮음 ~ 보통 |
| RandomForest      | 여러 Decision Tree 결합 | 과적합 감소, 안정적   | 학습 시간 증가      | 높음      |
| XGBoost           | Boosting 기반 트리 모델   | 매우 높은 예측 성능   | 파라미터 튜닝 필요    | 가장 높음   |
| SVR               | 거리 기반 회귀 모델         | 비선형 데이터 처리 가능 | Scaling 필수    | 보통 ~ 높음 |
| KMeans            | 비지도 군집화             | 데이터 패턴 그룹화 가능 | 예측 모델은 아님     | 군집 분석용  |

---- 

## 성능 그래프 

<img width="617" height="613" alt="image" src="https://github.com/user-attachments/assets/9fc106f1-fbc8-45a5-958a-4a2c689831f8" />

---

## 그래프 변환 원인 분석


Feature Scaling, Feature Selection,
Feature Engineering을 적용하여
데이터 품질을 개선하였고

| 모델  | Scaling 전 R² | Scaling 후 R² |
| --- | ------------ | ------------ |
| SVR | 0.78         | 0.987        |

| 모델  | Scaling 전 MSE | Scaling 후 MSE |
| --- | ------------- | ------------- |
| SVR | 0.45          | 0.019         |

| 상태       | 변수 개수 | R²   |
| -------- | ----- | ---- |
| 전체 변수 사용 | 25개   | 0.91 |
| 중요 변수 선택 | 15개   | 0.94 |
변수를 줄였더니 성능이 좋아짐

또한 GridSearchCV를 이용한
하이퍼파라미터 튜닝을 통해
모델 성능을 최적화하였다.

| 상태           | R²    |
| ------------ | ----- |
| 기본 XGBoost   | 0.91  |
| 튜닝 후 XGBoost | 0.984 |

| 상태           | MSE   |
| ------------ | ----- |
| 기본 XGBoost   | 0.25  |
| 튜닝 후 XGBoost | 0.024 |


비교 결과 XGBoost 모델이
가장 높은 성능을 보였으며,
RandomForest 또한 안정적인 결과를 나타냈다.

그래서 정리하면

Feature Scaling 은  변수들의 크기를 비슷하게 맞춰주는 작업을 해주었고
Feature Selection는 중요한 변수만 선택해서 최적화 해주었고
하이퍼 파라미터 튜닝은 여러 파라미터 조합 하고 교차 검증을 수행하여 최적 값을 만들어서 변환된거같습니다

---

# 📌 실제 사용 시나리오

## 누가 사용할 수 있는가?

1. 여드름 피부를 관리하는 일반 사용자
2. 피부 상태를 기록하고 관리하는 사용자
3. 피부 관리 서비스를 개발하는 앱 개발자
4. 생활 습관과 피부 상태의 관계를 분석하고 싶은 사용자

## 어떤 상황에서 사용할 수 있는가?

사용자가 자신의 생활 습관 데이터를 입력하면 머신러닝 모델이 피부 상태를 예측하여 건강 점수, 피부 점수, 분석 결과 및 추천 정보를 제공할 수 있다.

---

# 📊 데이터 규모 적절성

| 구분    | 내용                       |
| ----- | ------------------------ |
| ✅ 장점  | 머신러닝 모델 학습 및 실습용으로 적절    |
| ✅ 장점  | 모델 비교 및 성능 분석 가능         |
| ⚠️ 한계 | 실제 서비스 수준으로는 데이터 수가 부족함  |
| ⚠️ 한계 | 다양한 연령대와 피부 타입을 반영하기 어려움 |

---

# 📈 현실 환경에서 충분한 데이터를 확보할 수 있는가?

* 수면 시간
* 물 섭취량
* 스트레스 수준
* 식습관
* 피부 상태

### 데이터 확보 방법

* 설문조사를 통한 데이터 수집
* 실제 사용자 입력 데이터 수집
* 공개 데이터셋(Kaggle 등) 활용
* 피부 관련 추가 데이터셋 확보

따라서 현실적으로 데이터 확보는 가능하지만, 높은 정확도를 위해서는 더 많은 데이터가 필요하다.

---

# 💰 비용 및 리스크

## 비용

* Python 기반 오픈소스 라이브러리 사용
* 무료 데이터셋 활용 가능
* 개인 PC 환경에서 실행 가능
* 서버 비용이 거의 발생하지 않음

## 리스크

머신러닝 모델은 100% 정확하지 않기 때문에 잘못된 예측이 발생할 수 있다.

### 오분류 발생 시 위험

* 실제 피부 상태와 다른 결과 제공
* 부적절한 피부 관리 방법 추천
* 사용자가 결과를 과도하게 신뢰할 가능성
* 피부 상태 개선에 도움이 되지 않을 수 있음

따라서 본 프로젝트는 의료 진단 목적이 아닌 참고용 서비스로 활용해야 한다.

---

# ⚠️ 모델 한계

## 데이터 한계

현재 사용한 데이터셋은 수면 건강 데이터 기반으로 구성되어 있으며, 피부 상태를 직접 측정한 전문 피부 데이터가 아니다.

## 일반화 한계

* 모든 피부 타입에 적용하기 어려움
* 연령별 피부 특성 반영 부족
* 계절 변화 영향 반영 부족
* 호르몬 변화 반영 부족
* 유전적 요인 반영 부족

## 다른 환경에서도 일반화할 수 있는가?

현재 데이터 범위 내에서는 높은 성능을 보였지만, 새로운 사용자나 다른 환경에서는 동일한 성능을 보장할 수 없다.

보다 높은 일반화 성능을 위해서는 다양한 연령대, 피부 타입, 생활 습관을 포함한 대규모 데이터셋 확보가 필요하다.

즉, 학습 데이터와 다른 사용자에게는 동일한 결과를 보장할 수 없다.

---

발표 형식 

시연 7~10분 전체 프로젝트 과정 

시연질의응답 5분 심층 구술 평가

# 데이터 머신러닝 모델 실험 Colab
https://colab.research.google.com/drive/1ex2DMlim6Y9Qip76KlFq6nd9BvoYTYjL#scrollTo=ZBVbQBGFHzTj

# 실행방법
pyrhon app.py
