import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import google.generativeai as genai


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
    EMAIL_ADDRESS = "email@company.com" 
    EMAIL_PASSWORD = "supersecretpassword"  

    sender = "anything@company.com" #The Email you want to send from P.S. You can customize this if you have a domain
    sender_name = "Your Name" #Sender Name

    message = MIMEMultipart()
    message["From"] = f"{sender_name} <{sender}>"
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(message_body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server: 
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, email, message.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPException as error:
        print("Error sending email:", error)

genai.configure(api_key="YOUR_API_KEY") # get the API key from https://makersuite.google.com/app/apikey . It is FREE

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