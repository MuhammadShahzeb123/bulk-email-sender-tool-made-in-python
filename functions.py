import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import google.generativeai as genai
import unicodecsv
import streamlit as st

default_message = """
Hi |*FNAME*|,

I saw you are a growing company (Write more about this company so they can feel similarity). 

There are a lot of problems faced by companies like |*COMPANY*| (Search their industry and Niche to find out if they lack in Marketing and if they are tech phobic or not. If not then don't include this section)

The best part is... I have found the way to fix these

Just hit the Reply and I'll send you over a PDF explaining everything you need to know. OR JUST GIVE ME 15 MIN OF YOUR TIME AND I WILL BE THERE TO FIX YOUR PROBLEMS at https://calendly.com/zcops

Make sure have it fixed before your competitors get an edge on you

Best,
Shahzeb Naveed

P.S Don't wait for other to see if they get results. Start now and Start Early!!! 🚀✨
"""
default_author = "Alex Cattoni"
default_subject = "you might wanna have a look at this"

def personalize_email(email_template, first_name, last_name, company):
    """Personalizes the email text with various placeholders."""

    personalized_email = email_template.replace("|*FNAME*|", first_name)
    personalized_email = personalized_email.replace("|*LNAME*|", last_name)
    personalized_email = personalized_email.replace("|*COMPANY*|", company)
    personalized_email = personalized_email.replace("|*FULLNAME*|", f"{first_name} {last_name}")

    return personalized_email

def sendmail(email, subject, message_body):
    SMTP_SERVER = "smtpout.secureserver.net"  #Find the Outgoing Server smtp.google.com
    SMTP_PORT = 80  #Port 465 or 587, 80 works for me. Check what will work for you in the Video
    EMAIL_ADDRESS = "shahzeb@zcops.com" 
    EMAIL_PASSWORD = "Shahzeb@12345678&ilovehira"  

    sender = "shahzeb@zcops.com" #The Email you want to send from P.S. You can customize this if you have a domain
    sender_name = "Shahzeb from ZCopS" #Sender Name

    message = MIMEMultipart()
    message["From"] = f"{sender_name} <{sender}>"
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(message_body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server: 
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, email, message.as_string())
    except smtplib.SMTPException as error:
        raise error




genai.configure(api_key="YOU_API_KEY")

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config={
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    },
    safety_settings=[
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ],
)

def read_csv(file_object):
    csv_reader = unicodecsv.DictReader(file_object)
    return list(csv_reader)

def extract_data(csv_data):
    extracted_data = []

    for row in csv_data:
        first_name = row.get('First Name', '')
        last_name = row.get('Last Name', '')
        company = row.get('Company', '')
        email = row.get('Email', '')

        extracted_data.append({
            'First Name': first_name,
            'Last Name': last_name,
            'Company': company,
            'Email': email,
        })

    return extracted_data

def craft_message(csv_file,message=None,subject=None, author=None):
    data = read_csv(csv_file)
    extracted_data = extract_data(data)
    if subject is None:
        subject = default_subject
    if message is None:
        message = default_message
    if author is None:
        author = default_author
    for contact in extracted_data:
        first_name = contact["First Name"]
        last_name = contact["Last Name"]
        company = contact["Company"]
        email = contact["Email"]

        response = model.generate_content([f"I want you to improve this email a bit more personalized\n\nSearch about this {company} so that you can make the message more personalized. You have to change the message such that it reflects the value of this company. Make sure to copy {author} Style of Copywriting\n\nThis is the Message:\n{message}\n\nThank you\n\n\nNOTE:Don't change the variables like |*FNAME*| or anything similar.\n\nDon't write any welcome messges like 'I hope this message finds you well' because it look usual. I want something unique\n\nOnly Send the Email and don NOT include you text like'Here is the Email"])
        st.write(f"Email sent to {first_name} {last_name}")
        personalized_email = personalize_email(response.text, first_name, last_name, company)
        sendmail(email, subject, personalized_email)