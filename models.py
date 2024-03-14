from transformers import pipeline

from constants import HUGGINGFACE_BASE_URL
import requests
import os

def img2text_local(url):
    # Load the model
    image_to_text_model = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text_model(url)

    print(text)
    return text


def img2text(image_path):
    API_URL = f"{HUGGINGFACE_BASE_URL}Salesforce/blip-image-captioning-large"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

    with open(image_path, "rb") as f:
        data = f.read()

    response = requests.post(API_URL, headers=headers, data=data)
    print(response.json())
    output = response.json()[0]["generated_text"]
    print("Image scenario:", output)
    return output


def generate_story(scenario, n=20):
    template = """
    You are a story teller;
    You can generate a short sotry based on a scenario. The story should not be more than {n} words.
    Scenario: {scenario}

    Story:
    """

    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

    payload = {
        "inputs": template.format(scenario=scenario, n=n)
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    output = response.json()[0]["generated_text"]
    print(output)
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
