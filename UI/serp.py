from numpy import block
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import time
import random
import requests

st.set_page_config(page_title="SERPgen - Just Snip It!")

@st.cache(suppress_st_warning=True, show_spinner=False)
def intro():
    intro_container= st.empty()
    with intro_container:
        st.title("SERPgen 👨‍⚕️🔑✂️📃")
        time.sleep(2)
        st.image("./UI/SCALPEL_067.jpg", width= 200)
        time.sleep(2)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("# Just")
            time.sleep(0.5)
        with col2:
            st.write("# Snip")
            time.sleep(0.5)
        with col3:
            st.write("# It!")
            time.sleep(0.5)
        with col4:
            st.image("./UI/thumb_snip_sketch.webp", width= 200)
            time.sleep(2)
    # intro_container.empty()
    # with intro_container:
        with col1:
            st.write("Introducing")
            time.sleep(0.5)
        with col2:
            st.write("Team")
            time.sleep(0.5)
        with col3:
            st.write("OLAF")
            time.sleep(0.5)
        with col4:
            st.write("!!")
            time.sleep(1)
        with col1:
            st.image("./UI/Olaf.webp", width= 200)
            st.write("Olaf!")
            time.sleep(0.5)
        with col2:
            st.image("./UI/lenny.webp", width= 200)
            st.write("Lenard aka Lenny!")
            time.sleep(0.5)
        with col3:
            st.image("./UI/800px-Muhammad_Ali_NYWTS.jpg", width= 200)
            st.write("Alireza!")
            time.sleep(0.5)
        with col4:
            st.image("./UI/florida-map-color-coded-counties.jpg", width= 200)
            st.write("Florian!")
            time.sleep(7)

    intro_container.empty()

intro()

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

    url = 'https://api-serpgen-kw3vzvzkiq-ew.a.run.app/predict'
    params = {
        'key_list': key_list
    }
    response = requests.get(url, params=params)
    text=response.json()

    return text['prediction']

mod = st.radio("Choose ur input method!", ["I just wanna have FUN!", "I'm here 4 BUSINESS!", "Upload .csv-file"], key="mod")

if mod == "I just wanna have FUN!":
    keywords = st_tags(
        label='#### Enter Keywords:',
        text='Press enter to add more',
        #maxtags=3,
        key="keys1")

    but1, but2, but3 = st.columns(3)
    with but1:
        if st.button("Make your Keywords AWESOME! 🚀"):
            with st.spinner("AWESOMENESS in progress...💪"):
                st.write(key_to_text(keywords))
            st.balloons()
    with but2:
        if st.button("Make your Keywords SEXY! 👄"):
            sexy_cta = ['sexy', 'hot', 'cute', 'wild', 'stimulating',
                        'seductive', 'intriguing', 'tempting', 'provocative',
                        'appealing', 'desirable', 'sensual', 'exciting']
            keywords.insert(0, random.choice(sexy_cta))
            with st.spinner("Let me change real quick...👙"):
                st.write(key_to_text(keywords))
            st.snow()
    with but3:
        if st.button("SELL ME YOUR Keywords! 💸"):
            sell_cta = ['buy', 'purchase', 'order', 'sale', 'shop']
            keywords.insert(0, random.choice(sell_cta))
            with st.spinner("Bank balance increaing already...🤩"):
                st.write(key_to_text(keywords))
            st.snow()

elif mod == "I'm here 4 BUSINESS!":
    with st.form(key= "bus"):
        company_name = st.text_input('My Company is called:')
        purpose_type = st.radio('I am selling...💵', ['goods🍏', 'hands-on services👄', 'online services🌐', 'Just make me famous!😎'])
        keywords = st_tags(
        label='Enter Productname & 2 Attributes:',
        text='Press enter to add more',
        maxtags=3,
        key="keys2")
        submit = st.form_submit_button('BRING THE ACTION!🎬')

    urgent = ['now', 'fast', 'quick', 'hurry', 'rapidly', 'close', 'approaching', 'never', 'seconds', 'again', 'over',
              'instant', 'today', 'limited', 'few left', 'last']

    goods = ['buy', 'purchase', 'order', 'sale', 'shop', 'discover', 'acquire', 'get', 'take']

    servives = ['come', 'enjoy', 'feel', 'try', 'benefit', 'appreciate', 'relish']

    online = ['register', 'subscribe', 'join', 'be a part', 'try out', 'broadcast', 'discover', 'download', 'develop', 'invest', 'secure']

    famous = ['inform', 'check out', 'get to know', 'discover', 'find', 'locate', 'light on', 'come across']

    strong = ['shine', 'enlight', 'follow', 'reveal', 'absorb', 'advance', 'govern', 'gravitate', 'alter', 'scan',
              'amplify', 'attack', 'guide', 'beam', 'free', 'heighten', 'shine', 'shock', 'boost', 'broadcast', 'intensify',
              'capture', 'smash', 'launch', 'lead', 'locate', 'magnify', 'command', 'modify', 'multiply', 'steer', 'storm',
              'direct', 'perceive', 'picture', 'place', 'plant', 'engage', 'enlarge', 'transform', 'treat', 'position',
              'escort', 'power', 'expand', 'explore', 'explode', 'uncover', 'untangle', 'extend', 'unveil', 'extract',
              'refashion', 'usher', 'refine', 'weave', 'reveal', 'fuse', 'revitalize', 'revolutionize', 'gaze', 'rise',
              'train', 'fit', 'model', 'unlock', 'grow']

    targets = ['future', 'goal', 'dream', 'aim', 'cause', 'career', 'path', 'freedom', 'independence', 'will', 'success',
               'advantage', 'journey', 'power', 'knowledge', 'deal']
    if submit:
        pass #function

else:
    user_csv= st.file_uploader("Please provide your CSV!", type=["csv"])
    if user_csv:
        pass #csv-function
        st.balloons()

#if __name__ == "__main__":
