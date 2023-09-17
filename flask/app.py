import torch
from PIL import Image
import numpy as np
from flask import Flask, json, request
from py.bookmark_recommend import recommend_with_bookmark
from py.rating_recommend import find_favorite_genre_with_bookmark
from py.rating_recommend import recommend_with_ratings

app = Flask(__name__)

# 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='./yolo/best.pt', force_reload=True)

# 라벨 정보 로드
with open('./yolo/label.txt', 'r', encoding='utf-8') as label_file:
    labels = label_file.read().splitlines()

@app.route('/hello', methods=['GET'])
def hello():
    return "hello world"

@app.route('/detect', methods=['POST'])
def detect_ingredients():
    try:
        # 이미지 가져오기
        if 'image' in request.files:
            image = request.files['image']
            img = Image.open(image)

            # 이미지 크기를 1960으로 조정
            img = img.resize((1960, 1960))
            img = np.array(img)
            original_width, original_height = img.shape[1], img.shape[0]

            # 객체 인식 수행
            results = model(img, size=1960)

            # 객체 감지 결과를 원하는 형식으로 변환
            object_list = []
            for index, row in results.pandas().xyxy[0].iterrows():
                xmin = float(row['xmin']) * original_width / 1960
                ymin = float(row['ymin']) * original_height / 1960
                xmax = float(row['xmax']) * original_width / 1960
                ymax = float(row['ymax']) * original_height / 1960
                confidence = float(row['confidence'])
                class_index = int(row['class'])

                if class_index < len(labels):
                    label = labels[class_index]
                    item = {
                        "box": [xmin, ymin, xmax, ymax, confidence],
                        "tag": label
                    }
                    object_list.append(item)

            return json.dumps(object_list, ensure_ascii=False)
        else:
            return json.dumps({'error': 'No image file received'})
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route('/bookmark/recommend', methods=['GET'])
def get_bookmark_recommend():
    try:
        recipe_id = int(request.args.get('recipe_id'))
        page = int(request.args.get('page', 1))
    except (TypeError, ValueError):
        return json.dumps({"error": "Invalid parameters"}), 400
    try:
        # 추천 레시피 목록
        result = recommend_with_bookmark(recipe_id, 0, page)
    except KeyError as e:
        return json.dumps({"error": "Recipe ID not found"}), 404
    
    return json.dumps(result), 200

@app.route('/rating/recommend', methods=['GET'])
def get_rating_recommend():
    try:
        user_id = int(request.args.get('user_id'))
        page = int(request.args.get('page', 1))
        bookmark_list = request.args.getlist('bookmark_list', type=int)
    except (TypeError, ValueError):
        return json.dumps({"error": "Invalid parameters"}), 400
    try:
        # 가장 좋아하는 재료 장르 찾기
        user_id, favorite_genre = find_favorite_genre_with_bookmark(user_id, bookmark_list)
        # 추천 레시피 목록
        result = favorite_genre, recommend_with_ratings(user_id, favorite_genre, page)
    except KeyError as e:
        return json.dumps({"error": "User ID not found"}), 404
    
    return json.dumps(result), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)