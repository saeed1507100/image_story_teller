# image_story_teller
An AI demo app that will tell you a story based on the image you uploaded.

# Deploy locally

## 1. Add Environment variable
Add a .env file with hugging face api key like:
```
HUGGINGFACEHUB_API_TOKEN = "hf_...."
```

## 2. Install requirements
```
pip install -r requirements.txt
```

## 3. RUn the app with streamlit
```
streamlit run app.py
```