import streamlit as st
import csv
from functions import *

st.title("Send a lot of Emails")

subject = st.text_input("Subject... Write something unusual")
message = st.text_area("Write something that Gemini can edit. You don't need to write the full email yourself. Also, just tell the Niche of your Prospects to Gemini down the Variable")
niche = st.text_input("Niche: ")
autors = st.text_input("Enter the Copywriter you love | Copy his Style of Writing. ")
st.write("I like Alex Cattoni Writing Style")

uploaded_file = st.file_uploader("Upload a CSV file")

if st.button("Fire the Emails!!!"):
    if uploaded_file is not None:
        data = uploaded_file.read().decode("utf-8")  

        reader = csv.DictReader(data.splitlines())
        data = list(reader)
        

        for contact in data:
            first_name = contact["First Name"]
            last_name = contact["Last Name"]
            company = contact["Company"]
            email = contact["Email"]
            response = model.generate_content([f"I want you to improve this email a bit more personalized\n\nSearch about this {company} so that you can make the message more personalized. The Niche of this company is {niche} You have to change the message such that it reflects the value of this company. Make sure to copy {autors} Style of Copywriting\n\nThis is the Message:\n{message}\n\nThank you\n\n\nNOTE:Don't change the variables like |*FNAME*| or anything similar.\n\nDon't write any welcome messges like 'I hope this message finds you well' because it look usual. I want something unique\n\nOnly Send the Email and don NOT include you text like'Here is the Email"])

            personalized_email = personalize_email(response.text, first_name, last_name, company)
            sendmail(email, subject, personalized_email)