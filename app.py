from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import requests
import os

from constants import HUGGINGFACE_BASE_URL

load_dotenv(find_dotenv())

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
    print(response.json())
    return response.json()


if __name__ == "__main__":
    img2text("https://cdn.pixabay.com/photo/2018/03/11/20/42/mammals-3218028_640.jpg")