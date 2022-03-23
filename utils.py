from base64 import b64encode

from simpletransformers.language_generation import LanguageGenerationModel
import streamlit as st


TOP_K = 50
TOP_P = 0.95

MIN_LEN = 10
MAX_LEN = 50
DEFAULT_MAX_LEN = 20

HEIGHT = 200
MAX_CHARS = 1000


MODEL_ARGS = {
    'do_sample': True,
    'top_k': TOP_K,
    'top_p': TOP_P,
    'max_length': DEFAULT_MAX_LEN,
    'verbose': True,
}


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_model(**kwargs):
    return LanguageGenerationModel(
        'gpt2',
        'LM_outputs',
        use_cuda=False,
        args=kwargs,
    )


model = load_model(**MODEL_ARGS)

def run_model(text, **kwargs):
    return model.generate(text, args=kwargs)[0]


@st.cache(allow_output_mutation=True)
def png_to_base64(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return b64encode(data).decode()


def set_background(filename):
    binary = png_to_base64(filename)
    css_style = '''
        <style>
          .stApp {
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
          }
        </style>
    ''' % binary
    st.markdown(css_style, unsafe_allow_html=True)
