import datetime
import json
import os

import dateutil.parser
from google.oauth2 import service_account
from googleapiclient.discovery import build

INFO = json.loads(os.environ['GOOGLE_CLOUD_CREDS'])
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

credentials = service_account.Credentials.from_service_account_info(
    info=INFO,
    scopes=SCOPES
)

calendar_service = build('calendar', 'v3', credentials=credentials)

CALENDAR_ID = 'uncc.edu_voatgfp5jo8dhes4qlmqtn31c4@group.calendar.google.com'

EST = dateutil.tz.gettz('EST')
UTC = dateutil.tz.UTC


def parse(d):
    if 'date' in d:
        return dateutil.parser.parse(d['date']).date()
    else:
        return dateutil.parser.parse(d['dateTime'])


class Event:
    def __init__(self, htmlLink, start, description='', location='', summary='', **kw):
        self.html_link = htmlLink
        self.summary = summary
        self.description = description
        self.location = location
        self.start = parse(start)


def get_events(limit=10):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = calendar_service.events().list(calendarId=CALENDAR_ID,
                                                   timeMin=now,
                                                   maxResults=limit, singleEvents=True,
                                                   orderBy='startTime').execute()
    events = events_result.get('items', [])
    return [Event(**e) for e in events]
