import os
from dotenv import load_dotenv
from utils.extract import extract
from utils.transform import clean_data
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgresql

load_dotenv()

if __name__ == "__main__":
    raw_df = extract()
    if raw_df.empty:
        print("⚠️ Tidak ada data yang berhasil diambil.")
        exit()

    clean_df = clean_data(raw_df.to_dict(orient='records'))

    save_to_csv(clean_df)
    save_to_google_sheets(clean_df, os.getenv("GOOGLE_SHEETS_API"))
    save_to_postgresql(clean_df, os.getenv("DB_URL"))
