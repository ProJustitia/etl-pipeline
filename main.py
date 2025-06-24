import os
from dotenv import load_dotenv
from utils.extract import extract
from utils.transform import clean_data
from utils.load import save_to_csv, save_to_postgresql, save_to_google_sheets

load_dotenv()

raw_df = extract()
if raw_df.empty:
    print("⚠️ Tidak ada data yang berhasil diambil.")
    exit()

clean_df = clean_data(raw_df.to_dict(orient="records"))

save_to_csv(clean_df)

save_to_postgresql(clean_df, os.getenv("DB_URL"))

GOOGLE_SHEETS_JSON = os.getenv("GOOGLE_SHEETS_API")
GOOGLE_SHEETS_ID = "18j_FXgD08eOjxc_UbBS_WmJOk5CaQWGlqTtJceZQhV8"
GOOGLE_SHEETS_RANGE = "Sheet1!A1"

save_to_google_sheets(clean_df, GOOGLE_SHEETS_JSON, GOOGLE_SHEETS_ID, GOOGLE_SHEETS_RANGE)
