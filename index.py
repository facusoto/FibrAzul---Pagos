from datetime import datetime
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Variables para Google Sheets!
SAMPLE_SPREADSHEET_ID = '1qxFPVKq_nDM9bu-U7fDewd0h0hnRo9rRNf7Yy98TKIc'
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

# @execution_time
def execution():
    # Obtención de las contraseñas en google sheets
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range='Principal').execute()
    data = result.get('values')
    print('Completado: Datos copiados')
    print("------")
    return data

GS_EXPORT = execution()
df = pd.DataFrame(data=GS_EXPORT)

value = '19216837088'

print(df.loc[df[1] == value])


"""
# Google sheets requests, grabación de datos
def request_data():
    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                          range='Modems!D' + str(numero1), valueInputOption="USER_ENTERED",
                          body={"values": output_data}).execute()
"""
