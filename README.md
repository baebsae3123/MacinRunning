# MacinRunning
2학년1학기 머신러닝

## 여드름 피부 상태가 매일 달라서 뭐 써야할지에 대해 


# 백엔드

서버: http://127.0.0.1:5000/

사용모델: RandomForestRegressor

학습방법 : 지도 학습식

# 작동원리

데이터 입력 + 규칙 = 제품 추천 / 여드름 확률 계산 

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

