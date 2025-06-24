import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine

def save_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        print(f"CSV Save Error: {e}")


def save_to_google_sheets(df, json_keyfile, sheet_name="ETL Products"):
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
        client = gspread.authorize(creds)

        sheet = client.create(sheet_name)
        sheet.share('', perm_type='anyone', role='writer')

        worksheet = sheet.get_worksheet(0)

        df = df.copy()
        df['timestamp'] = df['timestamp'].astype(str)

        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    except Exception as e:
        print(f"Google Sheets Save Error: {e}")



def save_to_postgresql(df, db_url):
    try:
        engine = create_engine(db_url)
        df.to_sql('products', con=engine, index=False, if_exists='replace')
    except Exception as e:
        print(f"PostgreSQL Save Error: {e}")
