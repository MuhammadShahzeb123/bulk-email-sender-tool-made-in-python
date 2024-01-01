# Email Blaster with Gemini Personalization

Send personalized emails to multiple contacts, powered by AI-generated text from Gemini.

# Features:
    Streamlined web interface for easy email creation and sending
    Leverages Gemini for personalized email content
    Customizes emails based on recipient's company, niche, and preferred copywriting style
    Integrates with Gmail or any email service provider


# Requirements
    Python 3.7 or higher
    Streamlit
    CSV (Optional)
    smtplib
    email
    google-generativeai

A Google AI Maker Suite API key (get one for free at https://makersuite.google.com/app/apikey) and set the API_KEY in `functions.py`

# Installation
Clone this repository:

```Bash
git clone https://github.com/MuhammadShahzeb123/bulk-email-sender-tool-made-in-python.git
```

Or Download it in Zip File


Install the required libraries:

```Bash
cd bulk-email-sender-tool-made-in-python
pip install -r requirements.txt
```

Set your Gmail credentials or other email provider details in the functions.py file.

Obtain a Google AI Maker Suite API key and place it in the functions.py file.

# Usage
Run the Streamlit app:

```Bash
streamlit run Send_Emails_Using_Web_Browser.py
```

In your web browser, follow these steps:
    Enter a catchy subject line.
    Write a base email template, leaving room for personalization.
    Specify the niche of your target audience.
    Choose a copywriter whose style you want to emulate.
    Upload a CSV file containing contact information (name, company, email).
    Click "Fire the Emails!!!" to send personalized emails to all contacts.


# Additional Notes
For more advanced usage, run the main.py file directly, providing the CSV file path as input.
Customize the email template, subject line, and copywriting style to match your specific needs.
Consider adjusting the Gemini model configuration (temperature, top_p, top_k) for different content generation preferences.


# Contributing
We welcome contributions! Please feel free to submit pull requests or open issues.

Enjoy personalized email outreach with Gemini power!