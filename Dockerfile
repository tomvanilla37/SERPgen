FROM python:3.8.6-buster

COPY api /api
COPY notebooks/model /notebooks/model
#COPY model.joblib /model.joblib
COPY requirements.txt /requirements.txt
RUN python -m pip install --upgrade pip
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
