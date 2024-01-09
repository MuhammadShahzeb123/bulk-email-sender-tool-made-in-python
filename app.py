
from functions import *


st.header("Send a lot of Emails | Personalized!!")

uploaded_file = st.file_uploader("Upload CSV of Emails")

prompt_choice = st.radio(
    "Choose a prompt option:",
    options=["Use default", "Message and Subject  prompts"]
)

st.markdown("**Fire up ChatGPT**")
if prompt_choice == "Use default":
    if st.button("Send the Emails!!!"):
        craft_message(uploaded_file)

if prompt_choice == "Message and Subject  prompts":
    message = st.text_area("Input the template you want Gemini to Edit",value=default_message)
    subject = st.text_input("Subject", value=default_subject)
    author = st.text_input("CopyWriter | Who's Style you want to Copy", value=default_author)
    if st.button("Send the Emails!!"):
        craft_message(uploaded_file, message=message, author=author, subject=subject)