import gradio as gr
import perplexity_gradio

gr.load(
    name='llama-3.1-sonar-huge-128k-online',
    src=perplexity_gradio.registry,
).launch()