from pytest import param
import requests
import random
import pandas as pd

user_csv = ""  # dummy, can remain empty for single mode
#user_csv = pd.read_csv("Wowbow_Dog_Products.csv")   # uncomment to test mass mode
#user_csv2 = pd.read_csv("Wowbow_Dog_Services.csv")  # rename to user_csv to switch to services

SAMPLE_PARAMS = {"company_name": "XY Unlimited",
                 "company_claim": "the best shop in town!",
                 "product_name": "GingerGold",
                 "purpose_type": "selling goods",
                 "product_attributes": ["perfect hairstyle", "brush", "exclusive"],
                 "product_category": "hair brush",
                 "input_df": user_csv}


WORD_COLLECTION = {"GOODS": ['Buy', 'Purchase', 'Order', 'Shop', 'Discover', 'Acquire', 'Get', 'Take', 'Check out'],
                   "SERVICES": ['Sign up', 'Subscribe', 'Try', 'Get started', 'Learn More', 'Join us', 'Let\'s',
                                'Be the first to', 'Don\'t wait', 'Register', 'Subscribe', 'Join', 'Be a part',
                                'Try out', 'Discover', 'Download', 'Develop', 'Invest', 'Secure', 'Inform', 'Check out',
                                'Get to know', 'Find', 'Learn about'],
                   "URGENT": ['now', 'fast', 'quick', 'Better hurry', 'as soon as possible', 'seconds',
                              'Now is the time', 'there has never been a better time', 'instant', 'today', 'limited',
                              'stop searching']}


params_config_snippet = {             # default value; explaination/observations
        "max_length": 512,            # 512; max token length of prediction; 1024 not working
        "num_return_sequences": 3,    # 1; number of predictions to be returned; 5 max
        "num_beams": 7,               # 2; picks N best sequences so far and considers the probabilities of combination of all preceding words along with word in current position
        "top_k": 60,                  # 50; lower number = shorter sentence
        "top_p": 0.4,                 # 0.95; towards 0 = less creative/more accurate, towards 1 = more creative/random
        "do_sample": True,            # True;
        "repetition_penalty": 3.5,    # 2.5; avoid sentences that repeat themselves
        "length_penalty": 2.0,        # 1.0;
        "early_stopping": True,       # True;    False makes sentence longer (makes up stuff)
        "skip_special_tokens": True,  # True;    creates </s> at end of sentence
        "clean_up_tokenization_spaces": False # True}
}


params_config_cta = {
        "max_length": 256,            # 512
        "num_return_sequences": 2,    # 1
        "num_beams": 4,               # 2
        "top_k": 60,                  # 50
        "top_p": 0.90,                # 0.95
        "do_sample": True,            # True
        "repetition_penalty": 3.5,    # 2.5
        "length_penalty": 2.0,        # 1.0
        "early_stopping": True,       # True
        "skip_special_tokens": True,  # True
        "clean_up_tokenization_spaces": False   # True}
}


def key_to_text(
        key_list,                         # any keywords to generate sentences from
        max_length: int = 512,            # 512
        num_return_sequences: int = 2,    # 1
        num_beams: int = 5,               # 2
        top_k: int = 60,                  # 50
        top_p: float = 0.90,              # 0.95
        do_sample: bool = True,           # True
        repetition_penalty: float = 3.5,  # 2.5
        length_penalty: float = 1.0,      # 1.0
        early_stopping: bool = True,      # True
        skip_special_tokens: bool = True, # True
        clean_up_tokenization_spaces: bool = True):  # True
    """generate a sentence from keywords via API (K2T model)

    Args:
        key_list: list of str
    Returns:
        str (sentence made from keywords)

    """
    key_list = (map(lambda x: x.lower(), key_list))
    key_list = ",".join(key_list)
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
    response = requests.get(url, params=params)
    text=response.json()
    # print(response.request.url) #uncomment to check request url
    return text['prediction']


def check_claim(claim):
    """Check for punctuation after claim, othwise adds fullstop.

    Args:
        claim: the company claim/slogan input by the user.
    Return:
        the edited company claim/slogan

    """
    fullstop_list = ["!", "?", "."]
    if claim:
        claim = claim.capitalize()
        if claim[-1] in fullstop_list:
                pass
        else:
            claim += "."
        return claim
    else:
        pass


def gen_cta_goods(product_cat):
    """Generate call-to-action based on product category

    Args:
        product_cat: product category (such as "beer" or "dog leash")
    Returns:
        auto-generated str with call-to-action

    """
    cta_input_params = [random.choice(WORD_COLLECTION["GOODS"])+"!", product_cat, random.choice(WORD_COLLECTION["URGENT"])+'!']
    cta_goods_output = key_to_text(cta_input_params, **params_config_cta)
    return cta_goods_output


def gen_cta_services(service_cat):
    """Generate call-to-action based on service category

    Args:
        product_cat: service category (such as "beer" or "dog leash")
    Returns:
        auto-generated str with call-to-action

    """
    cta_input_params = [random.choice(WORD_COLLECTION["URGENT"])+"!", random.choice(WORD_COLLECTION["SERVICES"])+'!', service_cat]
    cta_goods_output = key_to_text(cta_input_params, **params_config_cta)
    return cta_goods_output


def gen_serp_goods(user_input_vals):
    """Generate SERP-text for goods (single mode only)

    Args:
        user_input_vals: dict w/ company/product info, input_df not used (dummy)
    Returns:
        processed str with SERP-text

    """
    product_description = (user_input_vals["product_category"] + ", " + ", ".join(user_input_vals["product_attributes"])).split(", ")
    api_output = key_to_text(product_description, **params_config_snippet)
    company_claim = check_claim(user_input_vals["company_claim"])

    serp_head = f"{user_input_vals['product_name']} by {user_input_vals['company_name']} - {company_claim}"
    merged_output = serp_head +' ' + api_output +' ' + gen_cta_goods(user_input_vals["product_category"])
    return merged_output


def gen_serp_services(user_input_vals):
    """Generate SERP-text for services (single mode only)

    Args:
        user_input_vals: dict w/ company/product info, input_df not used (dummy)
    Returns:
        processed str with SERP-text

    """
    product_description = (user_input_vals["product_category"]+", "+", ".join(user_input_vals["product_attributes"])).split(", ")
    api_output = key_to_text(product_description, **params_config_snippet)
    company_claim = check_claim(user_input_vals["company_claim"])

    serp_head = f"{user_input_vals['product_name']} from {user_input_vals['company_name']} - {company_claim}"
    merged_output = serp_head+' '+api_output+' '+gen_cta_services(user_input_vals["product_category"])
    return merged_output


def gen_serp_single(user_input_vals):
    """Check purpose type, run respective function (goods/services) for single queries

    Args:
        user_input_vals: dict w/ company/product info, input_df not used (dummy)
    Returns:
        processed str with SERP-text

    """
    if user_input_vals["purpose_type"] == "selling goods":
        serp_single_output = gen_serp_goods(user_input_vals)
    elif user_input_vals["purpose_type"] == "promoting services":
        serp_single_output = gen_serp_services(user_input_vals)
    return serp_single_output


def gen_serp_mass(user_input_vals):
    """Check purpose type, run respective function (goods/services) for single queries

    Args:
        user_input_vals: dict w/ company/product info, input_df including product info (csv)
    Returns:
        pandas df with modified "Output (SERP text)" column for each row

    """
    company_name = user_input_vals["company_name"]
    company_claim = user_input_vals["company_claim"]
    mass_serp_df = user_input_vals["input_df"].copy()

    for index, row in mass_serp_df.iterrows():
        product_name = row["Product/Service Name"]
        product_description = (row["Product Category"]+", "+row["Attributes"]).split(", ")     # this is a list
        product_category = row["Product Category"]
        company_claim = check_claim(company_claim)
        serp_api_output = key_to_text(product_description, **params_config_snippet)

        if user_input_vals["purpose_type"] == "selling goods":
            call_to_action = gen_cta_goods(product_category)
        elif user_input_vals["purpose_type"] == "promoting services":
            call_to_action = gen_cta_services(product_category)

        serp_output = f"{product_name} by {company_name} - {company_claim} {serp_api_output} {call_to_action}"
        print(serp_output)
        mass_serp_df.loc[index, ("Output (SERP text)")] = serp_output       #old syntax: df["column"].loc[index] wokring, but gave error/warning
    serp_mass_output = mass_serp_df
    return serp_mass_output


print(gen_serp_single(SAMPLE_PARAMS))   # testing single mode with SAMPLE PARAMS
#gen_serp_mass(SAMPLE_PARAMS).to_csv("output_test.csv") # uncomment to test mass mode
