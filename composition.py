import gradio as gr
import perplexity_gradio

with gr.Blocks() as demo:
    with gr.Tab("llama-3.1-sonar-large-128k-chat"):
        gr.load('llama-3.1-sonar-large-128k-chat', src=perplexity_gradio.registry)
    with gr.Tab("llama-3.1-sonar-huge-128k-online"):
        gr.load('llama-3.1-sonar-huge-128k-online', src=perplexity_gradio.registry)

demo.launch()