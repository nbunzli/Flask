FROM python:3.9.1

COPY app /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP="main.py"
ENTRYPOINT python -m flask run --host=0.0.0.0 --port=5000