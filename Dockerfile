FROM python:3.7.2

WORKDIR /Curry_Recommendation_System

RUN pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt

RUN mv flask/app.py .
RUN mv flask/csv .
RUN mv flask/py .

ENV FLASK_APP app.py

CMD ["flask", "run", "--host=0.0.0.0"]
