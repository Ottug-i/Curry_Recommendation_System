# -*- coding: utf-8 -*-
"""model_evaluation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yBdtshbwZioV1UqYgAM_Dj_1du2wpnfd
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, make_scorer

# 예시 사용자로 RMSE 계산
user_ratings = pd.read_csv('user_rating.csv')
curry_genres = pd.read_csv('../recipe/genres.csv')

user_ratings = user_ratings.merge(curry_genres, left_on='id', right_on='id')

user_profile = user_ratings[user_ratings['userId'] == 1]

X_train, X_test, y_train, y_test = train_test_split(user_profile[curry_genres.columns], user_profile['rating'], random_state=42, test_size=0.1)

lasso = Lasso(alpha=0.005)

lasso.fit(X_train, y_train)

predictions = lasso.predict(X_test)

mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print(rmse)