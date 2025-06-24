import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine

def save_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        print(f"CSV Save Error: {e}")


def save_to_google_sheets(df, json_keyfile, sheet_id, range_name):
    try:
        df["timestamp"] = df["timestamp"].astype(str)

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_key(sheet_id)
        worksheet = sheet.worksheet(range_name.split('!')[0])  # ambil nama sheet, misal 'Sheet1'

        worksheet.clear()
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        print("✅ Data berhasil disimpan ke Google Sheets.")

    except Exception as e:
        print(f"❌ Google Sheets Save Error: {e}")





def save_to_postgresql(df, db_url):
    try:
        engine = create_engine(db_url)
        df.to_sql('products', con=engine, index=False, if_exists='replace')
    except Exception as e:
        print(f"PostgreSQL Save Error: {e}")
