import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
import pandas as pd
from excel_scraper import *

df = pd.read_csv('data.csv')

with open('body.txt', 'r') as file:
    # Read the contents of the file into a string variable
    body = file.read()

with open('subject.txt', 'r') as file:
    # Read the contents of the file into a string variable
    subject = file.read()

SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

def sendMail(body, subject, recipient):
    service = build('gmail', 'v1', credentials=creds)
    message = MIMEText(body)
    message['to'] = recipient
    message['subject'] = subject
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None







#MAIN RUNNER CODE

cols = list(df.columns)
for i in range(0, len(df.index)):
    LocalRecipient = df["company_mail"][i]
    sendMail(replaceWords(body, cols, i), subject, LocalRecipient)
