import unittest
import os
import pandas as pd
from utils.load import save_to_csv

class TestLoad(unittest.TestCase):
    def test_save_csv(self):
        df = pd.DataFrame({"A": [1], "B": [2]})
        filename = "test_output.csv"
        save_to_csv(df, filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
