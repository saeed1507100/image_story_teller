from transformers import pipeline

from constants import HUGGINGFACE_BASE_URL
import requests
import os
from IPython.display import Audio

def img2text_local(url):
    # Load the model
    image_to_text_model = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text_model(url)

    print(text)
    return text


def img2text(url):
    API_URL = f"{HUGGINGFACE_BASE_URL}Salesforce/blip-image-captioning-large"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

    data = requests.get(url).content

    response = requests.post(API_URL, headers=headers, data=data)
    output = response.json()[0]["generated_text"]
    print("Image scenario:", output)
    return output


def generate_story(scenario):
    template = """
    You are a story teller;
    You can generate a short sotry based on a scenario. The story should not be more than 20 words.
    
    Scenario: {scenario}
    Story:
    """

    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

    payload = {
        "inputs": template.format(scenario=scenario)
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    output = response.json()[0]["generated_text"]
    output = output.split("Story:\n")[1]
    print("Story: ", output)

    return output


def text_to_speech(text):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)

    with open("audio.wav", "wb") as f:
        f.write(response.content)

    Audio("audio.wav", autoplay=True)