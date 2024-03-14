from dotenv import find_dotenv, load_dotenv
from models import img2text, generate_story, text_to_speech
from constants import IMAGE_URL

import streamlit as st

load_dotenv(find_dotenv())


def tell_story(image_path, no_of_words=20):
    print(f"no_of_words: {no_of_words}")
    scenario = img2text(image_path)
    story = generate_story(scenario, n=no_of_words)
    text_to_speech(story)

    return scenario, story


def main():
    st.title("AI Story Teller")
    st.header("AI Story Teller")

    uploded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploded_file is not None:
        st.image(uploded_file, caption="Uploaded Image.", use_column_width=True, width="25%")
        byte_data = uploded_file.getvalue()
        with open(uploded_file.name, "wb") as f:
            f.write(byte_data)

        st.write("Generating story based on the image...")
        number = st.selectbox("Select the number of words", [10, 20, 30, 40, 50])

        scenario, story = tell_story(uploded_file.name, no_of_words=number)

        with st.expander("Scenario"):
            st.write(scenario)
        with st.expander("Story"):
            st.write(story)
        text_to_speech(story)

        st.audio("audio.wav")
        


if __name__ == "__main__":
    main()
