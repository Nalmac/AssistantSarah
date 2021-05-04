from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from Models.Assistant import Assistant
from Controllers.CommandsController import CommandController
from random import randint

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def authenticate_calendar():
    creds = None
    if os.path.exists('Auth/token.json'):
        creds = Credentials.from_authorized_user_file('Auth/token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'Auth/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('Auth/token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

def main():
    service = authenticate_calendar()
    assistant = Assistant()
    commandController = CommandController(assistant, service=service)
    assistant.speak("Bonjour Monsieur. En quoi puis-je vous aider ?")
    while True:
        while assistant.actif:
            entree = assistant.listenAndProcess()
            if entree is not None:
                commandController.handleCommand(entree)
        while not assistant.actif:
            assistant.listenForCall()

if __name__ == '__main__':
    main()