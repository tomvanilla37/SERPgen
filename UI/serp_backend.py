from pytest import param
import requests
import random
import streamlit as st
import pandas as pd

#user_csv2 = pd.read_csv("Wowbow_Dog_Products.csv")
#user_csv = pd.read_csv("Wowbow_Dog_Services.csv")

SAMPLE_PARAMS = {"company_name": "XY Unlimited",
                 "product_name": "Cillit Bang 3000",
                 "purpose_type": "promoting services",   #selling goods #promoting services
                 "product_attributes": ["'Spee Powergel'", "best on market", "new formula", "removes bacteria", "!"],
                 "product_category": "washing detergent",
                 #"input_df": user_csv
                }


WORD_COLLECTION = {
                    "GOODS" : ['Buy', 'Purchase', 'Order', 'Shop', 'Discover', 'Acquire', 'Get', 'Take', 'Check out'],
                    "SERVICES" : ['Sign up', 'Subscribe', 'Try', 'Get started', 'Learn More', 'Join us', 'Let\'s', 'Be the first to',
                                  'Don\t wait', 'Register', 'Subscribe', 'Join', 'Be a part', 'Try out', 'Discover',
                                  'Download', 'Develop', 'Invest', 'Secure', 'Inform', 'Check out', 'Get to know', 'Discover', 'Find',
                                  'Locate', 'Learn about'],
                     "APPEALING" : ['hot', 'stimulating', 'intriguing', 'tempting', 'appealing', 'desirable', 'exciting'],
                     "URGENT" : ['now', 'fast', 'quick', 'hurry', 'as soon as possible', 'seconds', 'Now is the time',
                                'there has never been a better time', 'instant', 'today', 'limited', 'last', 'stop searching'],
                    "STRONG_VERBS" : ['shine', 'enlight', 'follow', 'reveal', 'absorb', 'advance', 'govern', 'gravitate', 'alter', 'scan',
                                'amplify', 'attack', 'guide', 'beam', 'free', 'heighten', 'shine', 'shock', 'boost', 'broadcast', 'intensify',
                                'capture', 'smash', 'launch', 'lead', 'locate', 'magnify', 'command', 'modify', 'multiply', 'steer', 'storm',
                                'direct', 'perceive', 'picture', 'place', 'plant', 'engage', 'enlarge', 'transform', 'treat', 'position',
                                'escort', 'power', 'expand', 'explore', 'explode', 'uncover', 'untangle', 'extend', 'unveil', 'extract',
                                'refashion', 'usher', 'refine', 'weave', 'reveal', 'fuse', 'revitalize', 'revolutionize', 'gaze', 'rise',
                                'train', 'fit', 'model', 'unlock', 'grow'],
                    "TARGET" : ['future', 'goal', 'dream', 'aim', 'cause', 'career', 'path', 'freedom', 'independence', 'will', 'success',
                                'advantage', 'journey', 'power', 'knowledge', 'deal']
                            }


params_config_snippet =    {
        "max_length": 512,          #512    ; 1024 not working
        "num_return_sequences": 3,    #1  ; 5 max
        "num_beams": 6,        #2
        "top_k": 60,            #50         lower number = shorter sentence
        "top_p": 0.5,            #0.95          towards 0 = less creative, towards 1 = more creative/random
        "do_sample": True,             #True
        "repetition_penalty": 3.5,    #2.5
        "length_penalty": 4.0,        #1.0
        "early_stopping": True,        #True       ; makes sentence longer (makes up stuff)
        "skip_special_tokens": True,   #True     ; creates </s> at end of sentence
        "clean_up_tokenization_spaces": True    #True}
}


params_config_cta =    {
        "max_length": 512,          #512    ; 1024 not working
        "num_return_sequences": 2,    #1  ; 5 max
        "num_beams": 5,        #2
        "top_k": 60,            #50         lower number = shorter sentence
        "top_p": 0.95,            #0.95          towards 0 = less creative, towards 1 = more creative/random
        "do_sample": True,             #True
        "repetition_penalty": 1.5,    #2.5
        "length_penalty": 1.0,        #1.0
        "early_stopping": True,        #True       ; makes sentence longer (makes up stuff)
        "skip_special_tokens": True,   #True     ; creates </s> at end of sentence
        "clean_up_tokenization_spaces": True    #True}
}


def key_to_text(
        key_list,
        max_length: int = 512,          #512    ; 1024 not working
        num_return_sequences: int = 2,    #1  ; 5 max
        num_beams: int = 5,        #2
        top_k: int = 60,            #50         lower number = shorter sentence
        top_p: float = 0.90,            #0.95          towards 0 = less creative, towards 1 = more creative/random
        do_sample: bool = True,             #True
        repetition_penalty: float = 3.5,    #2.5
        length_penalty: float = 1.0,        #1.0
        early_stopping: bool = True,        #True       ; makes sentence longer (makes up stuff)
        skip_special_tokens: bool = True,   #True     ; creates </s> at end of sentence
        clean_up_tokenization_spaces: bool = True,):    #True
    '''
    a funtion to get the list of keys and return a text
    input:
        key_list: list of str
    output
        text_out: strls
    '''
    key_list = (map(lambda x: x.lower(), key_list))
    key_list=",".join(key_list)
    #pre trained
    url = 'https://api-serpgen-kw3vzvzkiq-ew.a.run.app/predict'
    #version 1
    url = 'https://api-serpgen-v1-kw3vzvzkiq-ew.a.run.app/predict'
    params = {
        'key_list': key_list,
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
    response = requests.get(url, params = params)
    text=response.json()
    #print(response.request.url) #uncomment to check request url
    return text['prediction']


def gen_SERP_single(user_input_vals):
    if user_input_vals["purpose_type"] == "selling goods":
        SERP_single_output = gen_SERP_goods(user_input_vals)
    elif user_input_vals["purpose_type"] == "promoting services":
        SERP_single_output = gen_SERP_services(user_input_vals)
    return SERP_single_output



def gen_SERP_mass(user_input_vals):
    company_name = user_input_vals["company_name"]
    mass_serp_df = user_input_vals["input_df"].copy()



    for index, row in mass_serp_df.iterrows():
        product_name = row["Product/Service Name"]
        product_attributes = (row["Product Category"]+", "+row["Attributes"]).split(", ")
        product_category = row["Product Category"]
        serp_api_output = key_to_text(product_attributes, **params_config_snippet)

        if user_input_vals["purpose_type"] == "selling goods":
            call_to_action = gen_CTA_goods(product_category)
        elif user_input_vals["purpose_type"] == "promoting services":
            call_to_action = gen_CTA_services(product_category)

        serp_output = f"{product_name} by {company_name} - {serp_api_output} {call_to_action}"
        print(serp_output)
        mass_serp_df.loc[index, ("Output (SERP text)")] = serp_output       #old syntax: df["column"].loc[index] wokring, but gave error/warning
    SERP_mass_output = mass_serp_df
    return SERP_mass_output   #return pandas df


def gen_SERP_goods(user_input_vals):
    api_output = key_to_text(user_input_vals["product_attributes"], **params_config_snippet)
    serp_head = f"{user_input_vals['product_name']} by {user_input_vals['company_name']} - "
    merged_output = serp_head +' '+ api_output +' '+ gen_CTA_goods(user_input_vals["product_category"])
    return merged_output


def gen_SERP_services(user_input_vals): #for single modus only
    api_output = key_to_text(user_input_vals["product_attributes"], **params_config_snippet)
    serp_head = f"{user_input_vals['product_name']} from {user_input_vals['company_name']} - "
    merged_output = serp_head+ ' ' + api_output+ ' ' + gen_CTA_services(user_input_vals["product_category"])
    return merged_output


def gen_CTA_goods(product_vals): #input product c
        CTA_input_params = [(WORD_COLLECTION["URGENT"][0])+'!', (WORD_COLLECTION["GOODS"][0])+"!", product_vals]
        CTA_goods_output = key_to_text(CTA_input_params, **params_config_cta)
        return CTA_goods_output


def gen_CTA_services(product_vals):
    CTA_input_params = [random.choice(WORD_COLLECTION["URGENT"])+"!", random.choice(WORD_COLLECTION["SERVICES"])+'!', product_vals]
    CTA_goods_output = key_to_text(CTA_input_params, **params_config_cta)
    return CTA_goods_output

#print(gen_SERP_single(SAMPLE_PARAMS))
#gen_SERP_mass(SAMPLE_PARAMS).to_csv("output_test.csv")
