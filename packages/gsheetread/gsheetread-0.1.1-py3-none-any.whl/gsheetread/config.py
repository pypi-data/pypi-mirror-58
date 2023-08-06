from __future__ import print_function

import base64
import pickle
import os.path as pth
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


def get_token():
    flow = InstalledAppFlow.from_client_secrets_file(
        pth.abspath('~/.gsheetread.json'), SCOPES)
    creds = flow.run_local_server(port=0)
    token = base64.b64encode(pickle.dumps(creds))
    print("new token:{}".format(token))
    return token
