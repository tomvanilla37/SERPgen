import pandas as pd
import joblib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from keytotext import trainer
#import os

#path = os.getcwd()
#print(path)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2

model = trainer()
model.load_model( model_dir="./notebooks/model",use_gpu=False)

@app.get("/")
def index():
    return dict(greeting="hello")


@app.get("/predict")
def predict(key_list=""):       # 1
    '''
    predict a text from the list of keys
    input: "a,b,c"
        key_list: list of str
    output
        text_out: strls

    call uvicorn:
        uvicorn api.fast:app --reload
    query:
        http://127.0.0.1:8000/predict?key_list=ski,mountain,sky
    '''

    if key_list=="":
        text_out=None
    else:
        key_list=key_list.split(',')
        print(key_list)
        text_out=model.predict(key_list,use_gpu=False)

    prediction={'keys':key_list,'prediction':text_out}
    return prediction

if __name__ == "__main__":
    key_list=["ski", "mountain", "sky"]
    key_list=",".join(key_list)
    print(key_list)
    predict(key_list)
