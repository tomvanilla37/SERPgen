from numpy import block
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import time

block = st.container()
with block:
    st.title("SERPgen")
    time.sleep(3)
    st.image("SCALPEL_067.jpg")
    time.sleep(3)
    st.write("Just")
    time.sleep(2)
    st.write("Snip")
    time.sleep(2)
    st.write("It!")
    time.sleep(5)
    st.empty(block)

mod = st.radio("Choose ur input method!", ["Upload .csv-file", "Provide Keywords"])

if mod == "":
    st.stop

if mod == "Provide Keywords":
    keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    maxtags=3,
    key="keys1")

st.write("### Your choice:")
st.write(type(keywords))

if mod == "Upload .csv-file":
    user_csv= st.file_uploader("Please provide your CSV!", type=["csv"])
    if user_csv:
        pass #csv-function

if __name__ == "__main__":
    st.set_page_config(page_title="SERPgen - Just Snip It!")
