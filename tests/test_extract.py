import unittest
from utils.extract import extract
import pandas as pd

class TestExtract(unittest.TestCase):
    def test_extract_output(self):
        df = extract()
        self.assertIsInstance(df, pd.DataFrame)
        if not df.empty:
            self.assertIn('Title', df.columns)
            self.assertIn('Price', df.columns)
            self.assertIn('Rating', df.columns)

if __name__ == "__main__":
    unittest.main()
