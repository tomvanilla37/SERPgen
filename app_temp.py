import streamlit as st


'''
# SERPgen front
'''

import requests
def key_to_text(key_list):
    '''
    a funtion to get the list of keys and return a text
    input:
        key_list: list of str
    output
        text_out: strls
    '''
    key_list = (map(lambda x: x.lower(), key_list))
    key_list=",".join(key_list)

    url = 'https://api-serpgen-kw3vzvzkiq-ew.a.run.app/predict?key_list=ali,city,london,france'
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
    response = requests.get(url, params=params)
    text=response.json()

    return text['prediction']

key_list=["ski", "mountain", "sky"]

f'''
keys:\n
{key_list} \n
\n
text: \n
{key_to_text(key_list)}
'''
