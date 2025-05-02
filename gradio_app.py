import gradio as gr
from inference import predict
from convert_to_json import convert_to_json
from transformers import pipeline

pipe = pipeline(
    "text2text-generation",
    "SurAyush/title2metadata"
)

def gradio_interface(title, store, manufacturer):
    """
    Gradio interface function to predict the category of a product.
    """

    prediction = predict(pipe, title, store, manufacturer)
    try:
        json_output = convert_to_json(prediction)
    except Exception as e:
        json_output = {
            "error": str(e),
            "prediction": prediction
        }

    return json_output


article = "A mini-project to automate product categorization using a finetuned T5(encoder-decoder transformer)-small model. \nThe model is trained on a [dataset](https://huggingface.co/datasets/SurAyush/ProductTitle-To-Category) of product titles and their corresponding metadata. \nVisit the [GitHub repository](https://github.com/SurAyush/Title2MetaData) for more details."
title = "Product Title To Metadata Converter"
description = "A simple Gradio interface to convert product titles into metadata using a finetuned T5(encoder-decoder transformer)-small model."
example = [ 
    "Homefab India 2 Piece Velvet Window Curtains - 5 feet, Brown",
    "Homefab",
    "Homefab India"
]

interface = gr.Interface(
    gradio_interface,
    inputs=[
        gr.Textbox(label="Title"),
        gr.Textbox(label="Store"),
        gr.Textbox(label="Manufacturer")
    ],
    outputs=gr.JSON(label="Prediction"),
    title=title,
    examples = [example],
    description=description,
    article=article
)

interface.launch()


