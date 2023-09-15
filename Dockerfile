FROM python:3.7.2

WORKDIR /Curry_Recommendation_System

COPY flask/app.py .
COPY flask/csv ./csv
COPY flask/py ./py
COPY flask/yolo ./yolo
COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN apt-get install -y libgl1-mesa-glx

ENV FLASK_APP app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
