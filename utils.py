import streamlit as st


def init_page_config() -> None:
    st.set_page_config(
        page_title='ЛабаБоба!',
        page_icon='https://raw.githubusercontent.com/Mathematician2000/lababoba/master/icon.png',
    )

init_page_config()


def set_background(url: str) -> None:
    css_style = rf'''
        <style>
          .stApp {{
            background-image: url("{url}");
            background-size: 100%;
          }}
        </style>
    '''
    st.markdown(css_style, unsafe_allow_html=True)
