from base64 import b64encode
import re

from razdel import sentenize
from simpletransformers.language_generation import LanguageGenerationModel
import streamlit as st


def init_page_config():
    st.set_page_config(
        page_title='ЛабаБоба!',
        page_icon='icon.png',
    )

init_page_config()


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


class LabaBobaModel:
    def __init__(self, *args, **kwargs):
        self.model = LanguageGenerationModel(*args, **kwargs)
        self.output = ''

    def run_model(self, prompt, **kwargs):
        output = self.model.generate(prompt, args=kwargs)[0]
        continuation = re.sub(
            r'(?P<punct>[\.!?…»])(?P<ch>[А-ЯЁA-Z"«-])',
            r'\g<punct> \g<ch>',
            output[len(prompt):],
        )
        sentences = list(sent.text for sent in sentenize(continuation))
        if len(sentences) > 1 and sentences[-1][-1] not in '.!?…»':
            sentences.pop()
        continuation = ' '.join(sentences)
        self.output = f'**{prompt}** {continuation}'.replace('  ', ' ')

    def get_last_output(self):
        return self.output


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_model(**kwargs):
    return LabaBobaModel(
        'gpt2',
        'LM_outputs',
        use_cuda=False,
        args=kwargs,
    )

model = load_model(**MODEL_ARGS)


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
