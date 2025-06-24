from utils.load import save_to_csv
import os
import pandas as pd

def test_save_csv():
    df = pd.DataFrame({"A": [1], "B": [2]})
    save_to_csv(df, "test_output.csv")
    assert os.path.exists("test_output.csv")
    os.remove("test_output.csv")