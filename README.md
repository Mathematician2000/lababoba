# LabaBoba: have a talk with me!

A tiny conversational server app with a language generation model for fun.

Powered by `streamlit`. Based on **GPT-2**.

## Implementation details
+ Based on pretrained HF [GPT-2 model](https://huggingface.co/sberbank-ai/rugpt3small_based_on_gpt2)
+ Trained and evaluated on texts from [humor corpus](https://github.com/computational-humor/humor-recognition/tree/master/data)
+ Zero-shot [perplexity](https://en.wikipedia.org/wiki/Perplexity): $\approx 71.8518$
+ Perplexity after one trainig epoch: $\approx 49.0305$

## Features
+ Inference caching for performance optimization
+ Last incomplete sentence (if not the only one) is discarded [manually](https://github.com/natasha/razdel#usage)
+ AMAZING kitties and best front-end design ever!

**Be careful**: the net is a bit offensive thanks to the abovementioned corpus.
