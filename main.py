from functions import *
import csv

csv_file_path = input("CSV FILE LOCATION: ")

data = []
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)
    


subject = "you might wanna have a look at this"
message = """
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


autors = "Alex Cattoni or Justin Wlesh"

for contact in data:
    first_name = contact["First Name"]
    last_name = contact["Last Name"]
    company = contact["Company"]
    email = contact["Email"]

    response = model.generate_content([f"I want you to improve this email a bit more personalized\n\nSearch about this {company} so that you can make the message more personalized. You have to change the message such that it reflects the value of this company. Make sure to copy {autors} Style of Copywriting\n\nThis is the Message:\n{message}\n\nThank you\n\n\nNOTE:Don't change the variables like |*FNAME*| or anything similar.\n\nDon't write any welcome messges like 'I hope this message finds you well' because it look usual. I want something unique\n\nOnly Send the Email and don NOT include you text like'Here is the Email"])

    personalized_email = personalize_email(response.text, first_name, last_name, company)
    sendmail(email, subject, personalized_email)