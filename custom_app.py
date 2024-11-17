import gradio as gr
import perplexity_gradio

gr.load(
    name='llama-3.1-sonar-large-128k-chat',
    src=perplexity_gradio.registry,
    title='Perplexity-Gradio Integration',
    description="Chat with llama-3.1-sonar-large-128k-chat model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()