# `perplexity-gradio`

is a Python package that makes it very easy for developers to create machine learning apps that are powered by Perplexity's API.

# Installation

You can install `perplexity-gradio` directly using pip:

```bash
pip install perplexity-gradio
```

That's it! 

# Basic Usage

You should first save your Perplexity API key to this environment variable:

```bash
export PERPLEXITY_API_KEY=<your token>
```

Then in a Python file, write:

```python
import gradio as gr
import perplexity_gradio

gr.load(
    name='llama-3.1-sonar-large-128k-online',
    src=perplexity_gradio.registry,
).launch()
```

Run the Python file, and you should see a Gradio Interface connected to the model on Perplexity!

![ChatInterface](chatinterface.png)

# Customization 

Once you can create a Gradio UI from an OpenAI endpoint, you can customize it by setting your own input and output components, or any other arguments to `gr.Interface`. For example, the screenshot below was generated with:

```py
import gradio as gr
import perplexity_gradio

gr.load(
    name='llama-3.1-sonar-large-128k-online',
    src=perplexity_gradio.registry,
    title='Perplexity-Gradio Integration',
    description="Chat with llama-3.1-sonar-large-128k-online model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()
```
![ChatInterface with customizations](perplexity_gradio_custom.png)

# Composition

Or use your loaded Interface within larger Gradio Web UIs, e.g.

```python
import gradio as gr
import perplexity_gradio

with gr.Blocks() as demo:
    with gr.Tab("llama-3.1-sonar-large-128k-online"):
        gr.load('llama-3.1-sonar-large-128k-online', src=perplexity_gradio.registry)
    with gr.Tab("llama-3.1-sonar-small-128k-online"):
        gr.load('llama-3.1-sonar-small-128k-online', src=perplexity_gradio.registry)

demo.launch()
```

# Under the Hood

The `perplexity-gradio` Python library has two dependencies: `openai` and `gradio`. It defines a "registry" function `perplexity_gradio.registry`, which takes in a model name and returns a Gradio app.

# Supported Models

For a comprehensive list of available models and their specifications, please refer to the [Perplexity Model Cards documentation](https://docs.perplexity.ai/guides/model-cards).


Note: The Online LLMs' search subsystem does not attend to the system prompt. The system prompt can be used to provide instructions related to style, tone, and language of the response.

Note: if you are getting a 401 authentication error, then the OpenAI API Client is not able to get the API token from the environment variable. This happened to me as well, in which case save it in your Python session, like this:

```py
import os

os.environ["PERPLEXITY_API_KEY"] = ...
```