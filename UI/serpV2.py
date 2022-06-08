#import numpy
import pandas as pd
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import streamlit.components.v1 as components

#import random
from serp_backend import key_to_text, gen_SERP_single, gen_SERP_mass
from gstyle_output import gen_SERP_preview
#import serp_intro




st.set_page_config(page_title="SERPgen - Just Snip It!")

company_name = st.text_input('My Company is called:', key='com_nam')
purpose_type = st.radio('Purpose', ['selling goods', 'promoting services'])
input_mod = st.radio('Single query or mass query via csv-file?', ['Single', 'CSV-Upload'])
if input_mod == 'Single':
    prod, cat, keys = st.columns(3) #columns
    with prod:
        product_name = st.text_input('Provide your product name:', key='prod_nam')
    with cat:
        product_category = st.text_input('Provide your product category:', help = 'What kind of product are you offering?', key='prod_cat')
    with keys:
        product_attributes = st_tags(
        label='Please specify some attributes:',
        text ='Press enter to add more',
        #maxtags=3,
        key="keys2")
        st.caption('What kind of product are you offering? Let us know some details!')
    if st.button("Submit your choices!"):
        user_input_vals = {"company_name": company_name,
                "purpose_type": purpose_type,
                "product_name": product_name,
                "product_category": product_category,
                "product_attributes": product_attributes
                }
        with st.spinner("Creating your customized SERP Result..."):
            output_single = gen_SERP_single(user_input_vals)
            st.write(output_single)  #uncomment later
            ### google like out put +++###
            with st.expander('Preview your SERP-output in Google:'):
                components.html(gen_SERP_preview(user_input_vals, output_single))        #gen_SERP_preview outputs html for preview
                st.balloons()
else:
    user_csv= st.file_uploader("Please provide your CSV!", type=["csv"])
    if user_csv:
        input_df = pd.read_csv(user_csv)
        with st.expander('Preview of your file:'):
            st.dataframe(input_df)
    if st.button('SERP my csv.file!') and user_csv:
        if company_name != "":
            user_input_vals = {"company_name": company_name,
                    "purpose_type": purpose_type,
                    "input_df": input_df
                    }
            with st.spinner("Creating your customized SERPed CSV-file..."):
                output_df = gen_SERP_mass(user_input_vals)
                output_csv = output_df.to_csv()
                with st.expander('Preview of your SERPed-file:'):
                    st.dataframe(output_df)
                st.download_button('Download your "SERPed-CSV"-file', data=output_csv, file_name=f'{company_name}_SERPgen.csv')
        else: st.write('Please provide your company name!')

#if __name__ == "__main__":
