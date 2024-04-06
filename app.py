# import all Necessary Libraries
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# configure API by loading key from .env file. create one .env file and configure your google API Key
load_dotenv() # load environment variables

# configure key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


# initialize gemini pro model
def initialize_model(model_name="gemini-pro-vision"):
    model = genai.GenerativeModel(model_name)
    return model


# streamlit UI
st.title("Welcome To Invoice Information Extractor 🧑‍💻")
st.write("---")

# Take the input query from user
prompt = st.chat_input("Provide your information  ", key="prompt")

# interface to upload image
st.sidebar.title("Upload Your Invoice image !")
st.sidebar.write("---")
uploaded_image = st.sidebar.file_uploader("Click on Browse and drop your invoice !", type=["jpg", "png", "jpeg"])

def get_image_bytes(uploaded_image):
    if uploaded_image is not None:
        # read the uploaded image in bytes
        image_bytes = uploaded_image.getvalue()

        image_info = [
            {
            "mime_type": uploaded_image.type,
            "data": image_bytes
        }
        ]
        return image_info
    else:
        raise FileNotFoundError("Upload Valid image file!")


def get_response(model, model_behavior, image, prompt):
    response = model.generate_content([model_behavior, image[0], prompt])
    return response.text


# initialize the gemini-pro-vision
model = initialize_model("gemini-pro-vision")

if uploaded_image is not None: # file upload handling
    image = Image.open(uploaded_image)
    # display the invoice image
    st.image(image, caption="Your Invoice", use_column_width=True)



# set the model behavior using prompting 
model_behavior = """
Your are an expert who understand invoice overall structures and has deep knowledge on it.
We will upload the invoice image and you have to answer the question based on information 
present in the invoice image.
"""

# Process the Response
if  prompt:
    with st.spinner("Extracting yor Info Please wait..."):
    
        if len(prompt) > 0:
            # get uploaded image file in bytes
            image_info = get_image_bytes(uploaded_image)
            response = get_response(model, model_behavior, image_info, prompt)
            st.warning(f"🧑‍💼     {prompt}")
            st.info(f"👨‍🚀        {response}")
        else:
            st.error("Please Enter a Valid Prompt!")
