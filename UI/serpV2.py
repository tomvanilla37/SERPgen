from numpy import block
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import random
from serp_backend import key_to_text
import serp_intro

st.set_page_config(page_title="SERPgen - Just Snip It!")

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


    if submit:
        pass #function

else:
    user_csv= st.file_uploader("Please provide your CSV!", type=["csv"])
    if user_csv:
        pass #csv-function
        st.balloons()

#if __name__ == "__main__":
