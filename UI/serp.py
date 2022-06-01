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
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("### Just")
            time.sleep(0.5)
        with col2:
            st.write("### Snip")
            time.sleep(0.5)
        with col3:
            st.write("### It!")
            time.sleep(2)
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

    url = 'https://api-serpgen-kw3vzvzkiq-ew.a.run.app/predict?key_list=ali,city,london,france'
    params = {
        'key_list': key_list
    }
    response = requests.get(url, params=params)
    text=response.json()

    return text['prediction']

mod = st.radio("Choose ur input method!", ["Upload .csv-file", "Provide Keywords"], key="mod")

if mod == "Provide Keywords":
    keywords = st_tags(
        label='## Enter Keywords:',
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
            sell_cta = ['buy', 'purchase', 'order now', 'sale', 'shop']
            keywords.insert(0, random.choice(sell_cta))
            with st.spinner("Bank balance increaing already...🤩"):
                st.write(key_to_text(keywords))
            st.snow()

else:
    user_csv= st.file_uploader("Please provide your CSV!", type=["csv"])
    if user_csv:
        pass #csv-function
        st.balloons()

#if __name__ == "__main__":
