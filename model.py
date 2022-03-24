import re

from razdel import sentenize
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


class LabaBobaModel:
    def __init__(self, *args, **kwargs):
        self.model = LanguageGenerationModel(*args, **kwargs)
        self.output = ''

    def run_model(self, prompt, **kwargs):
        output = self.model.generate(prompt, args=kwargs)[0]
        puncts = '.!?…»'
        continuation = re.sub(
            r'(?P<punct>[\{puncts}])(?P<ch>[А-ЯЁA-Z"«-])',
            r'\g<punct> \g<ch>',
            output[len(prompt):],
        )

        sentences = list(sent.text for sent in sentenize(continuation))
        if len(sentences) > 1 and sentences[-1][-1] not in puncts:
            sentences.pop()
        continuation = ' '.join(sentences)

        output = f'**{prompt}** {continuation}'.replace('  ', ' ')
        for ch in pucnts:
            output = output.replace(f' {ch} ', f'{ch} ')
        self.output = output

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