FROM python:3.7.2

RUN git clone "https://github.com/Ottug-i/Curry_Recommendation_System.git"

WORKDIR /flask

RUN pip install -r requirements.txt

ENV FLASK_APP app.py

CMD ["flask", "run", "--host=0.0.0.0"]