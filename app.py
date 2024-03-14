from dotenv import find_dotenv, load_dotenv
from models import img2text, generate_story, text_to_speech
from constants import IMAGE_URL

load_dotenv(find_dotenv())


if __name__ == "__main__":
    scenario = img2text(IMAGE_URL)
    story = generate_story(scenario)
    text_to_speech(story)
