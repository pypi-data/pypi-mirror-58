import base64
import pandas as pd
from typing import AnyStr
from googleapiclient.discovery import build
import pickle
from google.auth.transport.requests import Request


def get_creds(creds_encoded: bytes):
    creds = pickle.loads(base64.b64decode(creds_encoded))
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        print("token had to be refreshed: new token: {}".format(
            base64.b64encode(pickle.dumps(creds))
        ))

    return creds


def get_df(creds_encoded: bytes, gsheet_id: AnyStr, tab, first_row_is_header=True):
    creds = get_creds(creds_encoded)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    sheet_range = "{}!A1:Z".format(tab)
    headers = None
    all_data = []
    result = sheet.values().get(spreadsheetId=gsheet_id, range=sheet_range).execute()
    values = result.get('values', [])

    if first_row_is_header:
        headers = values[0][:len(values[1])]
        all_data.extend(values[1:])
    else:
        all_data.extend(values)

    return pd.DataFrame(data=all_data, columns=headers)


def jupyter_get_df(gsheet_id: AnyStr, tab, first_row_is_header=True):
    creds = input().encode('utf-8')
    return get_df(creds, gsheet_id, tab, first_row_is_header)
