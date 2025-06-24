# tests/test_load.py
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import save_to_google_sheets, save_to_postgresql

class TestLoad(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "Title": ["Test"],
            "Price": ["100"],
            "Rating": ["5"],
            "timestamp": ["2025-06-25T01:00:00"]
        })


    @patch("utils.load.gspread.authorize")
    @patch("utils.load.ServiceAccountCredentials.from_json_keyfile_name")
    def test_save_to_google_sheets(self, mock_creds, mock_auth):
        mock_client = MagicMock()
        mock_sheet = MagicMock()
        mock_worksheet = MagicMock()

        mock_creds.return_value = MagicMock()
        mock_auth.return_value = mock_client
        mock_client.open_by_key.return_value = mock_sheet
        mock_sheet.worksheet.return_value = mock_worksheet

        save_to_google_sheets(
            self.df,
            "fake.json",
            "sheet_id_dummy",
            "Sheet1!A2"
        )

        mock_worksheet.update.assert_called_once()



    @patch("utils.load.create_engine")
    def test_save_to_postgresql(self, mock_engine):
        mock_conn = mock_engine.return_value.connect.return_value
        save_to_postgresql(self.df, "postgresql://user:pass@localhost:5432/test_db")
        self.assertTrue(mock_engine.called)

if __name__ == "__main__":
    unittest.main()
