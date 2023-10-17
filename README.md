# 카레: 카메라로 찍고 레시피 추천받자! 🍛
현대인의 건강한 식습관 형성을 위한 식재료 인식 및 맞춤 레시피 추천 어플리케이션<br/><br/> 

## 🛠 레시피 추천 기술 스택
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
<br><br>

## 🗂 데이터 크롤링
- BeautifulSoup으로 '만개의 레시피' 크롤링
- 레시피를 25개의 재료로 분류<br><br>
![데이터 크롤링](https://github.com/Ottug-i/Curry_Recommendation_System/assets/87821678/03bf71b2-13bb-4e53-a329-c82bc76d67a7)
<br><br>

## ⚙ 모델 학습
- 재료 분류에 따라 서비스의 예상 사용자 페르소나 작성
- 25개의 재료 분류를 독립 변수로 하여 레시피의 평점을 예측하는 선형 회귀 Lasso 모델 학습<br><br>
![모델 학습](https://github.com/Ottug-i/Curry_Recommendation_System/assets/87821678/48f2f6a4-3210-4f5c-9893-5c0814029f8e)
<br><br>

## 📍 모델 탑재
- 학습한 모델을 Flask에 탑재하여 API 작성
- 사용자의 레시피 평점 정보를 기반으로 레시피 10개 추천
- 북마크한 레시피와 비슷한 레시피 5개 추천<br><br>
![API](https://github.com/Ottug-i/Curry_Recommendation_System/assets/87821678/e9e03a63-c18e-4cbc-b216-f93f24906fe9)
![모델 탑재1](https://github.com/Ottug-i/Curry_Recommendation_System/assets/87821678/4d7e565d-af1e-496f-8d6c-30f6a0c18501)
![모델 탑재2](https://github.com/Ottug-i/Curry_Recommendation_System/assets/87821678/401c405b-3f93-4465-b10a-d265f74521ab)
<br><br>

## 👩🏻‍💻 머신러닝 개발자
| 김가경 | 김희서 |
| :-: | :-: |
| [@GaGa-Kim](https://github.com/GaGa-Kim) | [@rlaltj](https://github.com/hap6v6) |
|<img src="https://github.com/GaGa-Kim.png" style="width:150px; height:150px;">|<img src="https://avatars.githubusercontent.com/u/76986589?v=4" style="width:150px; height:150px;">||
