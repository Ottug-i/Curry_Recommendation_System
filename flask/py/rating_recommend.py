import pymysql
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso

def find_favorite_genre_with_bookmark(user_id, bookmark_list):
    
    if not bookmark_list:
        return user_id, None
    
    curry_recipes = pd.read_csv('./csv/curry_recipe_with_genres.csv', index_col='id')

    genre_count = {}
    for recipe_id in bookmark_list:
        genres = curry_recipes.loc[recipe_id, 'genres'].split('|')
        for genre in genres:
            genre_count[genre] = genre_count.get(genre, 0) + 1

    favorite_genre = max(genre_count, key=genre_count.get)
    return user_id, favorite_genre

def recommend_with_ratings(user_id, favorite_genre, page):

    db = pymysql.connect(host='{MYSQL_URL}', port=3306, user='{MYSQL_USERNAME}', password='{MYSQL_PW}', db='curry', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    try:
        with db.cursor() as cursor:
            sql = "SELECT * FROM curry.ratings"
            cursor.execute(sql)
            user_ratings = pd.DataFrame(cursor.fetchall())
            print(user_ratings)

            curry_genres = pd.read_csv('./csv/genres.csv')

            user_ratings = user_ratings.merge(curry_genres, left_on='recipe_id', right_on='id')
            print(user_ratings)

            user_profile = user_ratings[user_ratings['user_id'] == user_id]

            lasso = Lasso(alpha=0.005)

            lasso.fit(user_profile[curry_genres.columns], user_profile['rating'])

            predictions = lasso.predict(curry_genres)
            curry_genres['predict'] = predictions

            if favorite_genre is None:
                sorted_user_predict = curry_genres.sort_values(by='predict', ascending=False)
            else:
                sorted_user_predict = curry_genres.sort_values(by=['predict', favorite_genre], ascending=[False, False])

            user_predict_ids = sorted_user_predict.id.tolist()

            start_idx = (page - 1) * 10
            end_idx = start_idx + 10

            if start_idx >= len(user_predict_ids):
                return None

            return user_predict_ids[start_idx:end_idx]
    
    finally:
        db.close()