import pandas as pd
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import streamlit.components.v1 as components

from serp_backend import key_to_text, gen_serp_single, gen_serp_mass
from gstyle_output import gen_SERP_preview

st.set_page_config(page_title="SERPgen - Just Snip It!")
#st.image(image='./UI/cut_logo.png', use_column_width = True)
col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    st.write("")
with col3:
    st.image(image='./UI/cut_logo.png', use_column_width = True)

nam, claim = st.columns(2)
with nam:
    company_name = st.text_input('Company name:', key='com_nam')
with claim:
    company_claim = st.text_input('Company\'s claim:', help= 'short description/slogan or claim of your company', key='com_cla')
purp, mod = st.columns(2)
with purp:
    purpose_type = st.radio('Purpose', ['selling goods', 'promoting services'])
with mod:
    input_mod = st.radio('Single query or mass query via Excel-file?', ['Single', 'Excel-Upload'])
if input_mod == 'Single':
    prod, cat, keys = st.columns(3)
    with prod:
        product_name = st.text_input('Product name:', key='prod_nam')
    with cat:
        product_category = st.text_input('Category of product/service:', help = 'What kind of product are you offering?', key='prod_cat')
    with keys:
        product_attributes = st_tags(
        label= ('Features of the product/service:'),
        text ='Press enter to add more',
        #value = ['unique'],
        #maxtags=3,
        key="keys2")
        st.caption('What kind of product are you offering? Let us know some details!')
    if st.button("Submit your choices!"):
        user_input_vals = {"company_name": company_name,
                "company_claim": company_claim,
                "purpose_type": purpose_type,
                "product_name": product_name,
                "product_category": product_category,
                "product_attributes": product_attributes
                }
        if product_attributes:
            with st.spinner("Creating your customized SERP Result..."):
                output_single = gen_serp_single(user_input_vals)
                st.markdown(f'> {output_single}')
                ### google like out put +++###
                with st.expander('Preview your SERP-output in Google:'):
                    print(user_input_vals["product_category"])
                    html = gen_SERP_preview(user_input_vals, output_single)
                    components.html(html)
                    st.balloons()
        else: st.write('Please provide some attributes of your product!')
else:
    user_file= st.file_uploader("Please provide your Excel-file!", type=["xls", "xlsx", "xlsm", "xlsb", "odf", "ods", "odt", "csv"])
    if user_file:
        input_df = pd.read_csv(user_file)
        with st.expander('Preview of your file:'):
            st.dataframe(input_df)
    if st.button('SERP my file!') and user_file:
        if company_name != "":
            user_input_vals = {"company_name": company_name,
                               "company_claim": company_claim,
                                "purpose_type": purpose_type,
                                "input_df": input_df
                                }
            with st.spinner("Creating your customized SERPed Excel-file..."):
                output_df = gen_serp_mass(user_input_vals)
                output_csv = output_df.to_csv()
                with st.expander('Preview of your SERPed-file:'):
                    st.dataframe(output_df)
            if output_csv:
                st.download_button('Download your "SERPed-CSV-file"', data=output_csv, file_name=f'{company_name}_SERPgen.csv')

        else: st.write('Please provide your company name!')

#if __name__ == "__main__":
