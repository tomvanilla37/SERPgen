from numpy import block
import pandas as pd
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import random
from serp_backend import key_to_text
import serp_intro

st.set_page_config(page_title="SERPgen - Just Snip It!")

company_name = st.text_input('My Company is called:', key='com_nam')
purpose_type = st.radio('Purpose', ['selling goods', 'promoting services', 'exposure/publicity'])
input_mod = st.radio('Single query or mass query via csv-file?', ['Single', 'CSV-Upload'])
if input_mod == 'Single':
    prod, keys = st.columns(2)
    with prod:
        product_name = st.text_input('Provide your product name:', key='prod_nam')
    with keys:
        product_attributes = st_tags(
        label='Please specify some attributes:',
        text ='Press enter to add more',
        #maxtags=3,
        key="keys2")
        st.caption('What kind of product are you offering? Let us know some details!')
    if st.button("Submit your choices!"):
        params = {"company_name": company_name,
                "purpose_type": purpose_type,
                "product_name": product_name,
                "product_attributes": product_attributes
                }
        with st.spinner("Creating your customized SERP Result..."):
            pass #output_single = gen_SERP_single(params)
        st.markdown(
                    # '''
                    # <font face="Arial" size="14px" color="#006621">https://wooptor.com > products > woopto-classic-red</font><br>
                    # <font face="Arial" size="18px" color="#1a0dab">Woopto Classic Red Dog Collar and Leash - Wooptor</font><br>
                    # <font face="Arial" size="13px" color="#545454">Woopto Classic Red Dog Collar and Leash - Comfortable, durable and stylish dog collars</font>
                    # '''
                    '''
                    <div class= 'container'>
                    .container {display:flex;}</div>
                        <div class= 'link'>
                        <p><font face="Arial" size="14px" color="#006621">https://wooptor.com > products > woopto-classic-red</font></p>
                        <p><font face="" size="18px" color="#1a0dab">Woopto Classic Red Dog Collar and Leash - Wooptor</font></p>
                        <p><font face="Arial" size="13px" color="#545454">Woopto Classic Red Dog Collar and Leash - Comfortable, durable and stylish dog collars</font></p>
                        </div>
                        <div class= 'google-image'>
                        .google-image{<img src="https://cdn.shopify.com/s/files/1/0024/6025/4254/products/bunte-Leinen-und-Halsbaender-rot-L-2_1x1.jpg?v=1638825557" object-fit: contain; </img>}</div>
                    '''
                    , unsafe_allow_html=True)

else:
    user_csv= st.file_uploader("Please provide your CSV!", type=["csv"])
    if user_csv:
        input_df = pd.read_csv(user_csv)
        with st.expander('Preview of your file:'):
            st.dataframe(input_df)
        params = {"company_name": company_name,
                 "purpose_type": purpose_type
                }
        with st.spinner("Creating your customized SERPed CSV-file..."):
            pass #output_csv = df.to_csv(gen_SERP_mass(params))
        st.download_button('Download your "Serped-CSV"-file', data=output_csv, file_name=f'{company_name}_SERPgen.csv')

#if __name__ == "__main__":
