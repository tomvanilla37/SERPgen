from pytest import param
import requests
import random
import streamlit as st
import pandas as pd

#user_csv = pd.read_csv("/home/tomvanilla/code/tomvanilla37/final project/data/Wowbow_Dog_Products.csv")

SAMPLE_PARAMS = {"company_name": "XY Unlimited",
                 "product_name": "Cillit Bang 3000",
                 "purpose_type": "selling goods",
                 "product_attributes": ["'Spee Powergel'", "washing detergent", "best on market", "new formula", "removes bacteria"],
                 #"input_df": user_csv
                }




def key_to_text(key_list):
    '''
    a funtion to get the list of keys and return a text
    input:
        key_list: list of str
    output
        text_out: strls
    '''
    #key_list = (map(lambda x: x.lower(), key_list))                 #why only lowercase input
    key_list = ",".join(key_list)

    url = "https://api-serpgen-v1-kw3vzvzkiq-ew.a.run.app/predict"
    old_url = 'https://api-serpgen-kw3vzvzkiq-ew.a.run.app/predict'
    params = {
        'key_list': key_list,
        'num_beams': 4             # crashes if below 1, stupid results if 1, from 6 on makes "best" to "best-selling", 7 includes more keywords (cf. dog sandals)
    }
    response = requests.get(url, params=params)
    text=response.json()
    #print(response.request.url) #uncomment to check request url
    return text['prediction']


def gen_SERP_single(params):
    if params["purpose_type"] == "selling goods":
        SERP_single_output = gen_SERP_goods(params)
    elif params["purpose_type"] == "promoting services":
        SERP_single_output = gen_SERP_services(params)
    return SERP_single_output


def gen_SERP_mass(params):
    company_name = params["company_name"]

    #if params["purpose_type"] == "selling goods":    #uncomment and change indentation later to enable differed modes (goods, services, etc)
    mass_serp_df = params["input_df"].copy()
    for index, row in mass_serp_df.iterrows():
        product_name = str(row["Product/Service Name"])
        product_attributes = row["Attributes"].split(", ")
        serp_api_output = key_to_text(product_attributes)
        serp_output = f"{product_name} by {company_name} - {serp_api_output}"
        print(serp_output)
        mass_serp_df.loc[index, ("Output (SERP text)")] = serp_output       #old syntax: df["column"].loc[index] wokring, but gave error/warning
    SERP_mass_output = mass_serp_df
    return SERP_mass_output   #return pandas df


def gen_SERP_goods(params):
    api_output = key_to_text(params["product_attributes"])
    serp_head = f"{params['product_name']} by {params['company_name']} - "
    merged_output = serp_head+api_output # +gen_CTA_goods()
    return merged_output

def gen_SERP_services(params):
    api_output = key_to_text(params["product_attributes"])
    serp_head = f"{params['product_name']} from {params['company_name']} - "
    merged_output = serp_head+api_output # +gen_CTA_services()
    return merged_output



def gen_CTA_goods(params):
    pass

def gen_CTA_services(params):
    pass

def list_collection():
    goods = ['buy', 'purchase', 'order', 'sale', 'shop', 'discover', 'acquire', 'get', 'take']

    services = ['come', 'enjoy', 'feel', 'try', 'benefit', 'appreciate', 'relish']

    online = ['register', 'subscribe', 'join', 'be a part', 'try out', 'broadcast', 'discover', 'download', 'develop', 'invest', 'secure']

    famous = ['inform', 'check out', 'get to know', 'discover', 'find', 'locate', 'light on', 'come across']

    appealing = ['sexy', 'hot', 'cute', 'wild', 'stimulating',
                        'seductive', 'intriguing', 'tempting', 'provocative',
                        'appealing', 'desirable', 'sensual', 'exciting']

    urgent = ['now', 'fast', 'quick', 'hurry', 'rapidly', 'close', 'approaching', 'never', 'seconds', 'again', 'over',
              'instant', 'today', 'limited', 'few left', 'last']

    strong = ['shine', 'enlight', 'follow', 'reveal', 'absorb', 'advance', 'govern', 'gravitate', 'alter', 'scan',
              'amplify', 'attack', 'guide', 'beam', 'free', 'heighten', 'shine', 'shock', 'boost', 'broadcast', 'intensify',
              'capture', 'smash', 'launch', 'lead', 'locate', 'magnify', 'command', 'modify', 'multiply', 'steer', 'storm',
              'direct', 'perceive', 'picture', 'place', 'plant', 'engage', 'enlarge', 'transform', 'treat', 'position',
              'escort', 'power', 'expand', 'explore', 'explode', 'uncover', 'untangle', 'extend', 'unveil', 'extract',
              'refashion', 'usher', 'refine', 'weave', 'reveal', 'fuse', 'revitalize', 'revolutionize', 'gaze', 'rise',
              'train', 'fit', 'model', 'unlock', 'grow']

    targets = ['future', 'goal', 'dream', 'aim', 'cause', 'career', 'path', 'freedom', 'independence', 'will', 'success',
               'advantage', 'journey', 'power', 'knowledge', 'deal']


#print(gen_SERP_single(SAMPLE_PARAMS))
#gen_SERP_mass(SAMPLE_PARAMS).to_csv("output_test.csv")
