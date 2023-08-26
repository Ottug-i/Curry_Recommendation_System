FROM python:3.7.2

RUN git clone "https://github.com/Ottug-i/Curry_Recommendation_System.git"

WORKDIR /Curry_Recommendation

RUN pip install -r requirements.txt

RUN mv Curry_Recommendation_System/flask/app.py .
RUN mv Curry_Recommendation_System/flask/csv .
RUN mv Curry_Recommendation_System/flask/py .

ENV FLASK_APP app.py

CMD ["flask", "run", "--host=0.0.0.0"]
