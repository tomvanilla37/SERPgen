import pandas as pd
import joblib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from keytotext import trainer
from memoized import memoized

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

@memoized
def load_model(model_name):
    model = trainer()
    model.load_model( model_dir=f"./notebooks/{model_name}",use_gpu=False)
    return model

@app.get("/")
def index():
    return dict(greeting="hello")


@app.get("/predict")
def predict(
        key_list: str = "",
        max_length: int = 512,
        num_return_sequences: int = 1,
        num_beams: int = 2,
        top_k: int = 50,
        top_p: float = 0.95,
        do_sample: bool = True,
        repetition_penalty: float = 2.5,
        length_penalty: float = 1.0,
        early_stopping: bool = True,
        skip_special_tokens: bool = True,
        clean_up_tokenization_spaces: bool = True,
        ):       # 1
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
    params={
        'max_length':  max_length,
        'num_return_sequences':  num_return_sequences,
        'num_beams':  num_beams,
        'top_k':  top_k,
        'top_p':  top_p,
        'do_sample':  do_sample,
        'repetition_penalty':  repetition_penalty,
        'length_penalty':length_penalty,
        'early_stopping':  early_stopping,
        'skip_special_tokens':  skip_special_tokens,
        'clean_up_tokenization_spaces':  clean_up_tokenization_spaces,
    }
    print(params)
    if key_list=="":
        text_out=None
    else:
        model=load_model('modelv1')
        key_list=key_list.split(',')
        print(key_list)
        text_out=model.predict(key_list,use_gpu=False,**params)

    prediction={'keys':key_list,'prediction':text_out}

    return prediction

if __name__ == "__main__":
    key_list=["ski", "mountain", "sky"]
    key_list=",".join(key_list)
    print(key_list)

    params= {"do_sample":True, "num_beams":4, "early_stopping":True,'num_return_sequences':4}

    print('first')
    print(predict(key_list,**params))

    #print('second')
    #print(predict(key_list))
