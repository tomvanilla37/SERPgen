import streamlit as st
import time

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
