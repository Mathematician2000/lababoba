from base64 import b64encode

import streamlit as st


def init_page_config():
    st.set_page_config(
        page_title='ЛабаБоба!',
#        page_icon='icon.png',
        page_icon='https://raw.githubusercontent.com/Mathematician2000/lababoba/master/icon.png',
    )

init_page_config()


@st.cache(allow_output_mutation=True)
def png_to_base64(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return b64encode(data).decode()

"""
def set_background(filename):
    binary = png_to_base64(filename)
    css_style = fr'''
        <style>
          .stApp {{
            background-image: url("data:image/png;base64,{binary}") left top no-repeat;
            background-size: 100%;
          }}
        </style>
    '''
    st.markdown(css_style, unsafe_allow_html=True)
"""

def set_background(url):
    css_style = fr'''
        <style>
          .stApp {{
            background-image: url("{url}");
            background-size: 100%;
          }}
        </style>
    '''
    st.markdown(css_style, unsafe_allow_html=True)
