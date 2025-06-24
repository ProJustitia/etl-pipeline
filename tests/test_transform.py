import unittest
from utils.transform import clean_data
import pandas as pd

class TestTransform(unittest.TestCase):
    def test_transform_types(self):
        sample = [{
            'Title': 'Cool Shirt',
            'Price': '$10',
            'Rating': '4.5 / 5',
            'Colors': '3 Colors',
            'Size': 'Size: M',
            'Gender': 'Gender: Men',
            'timestamp': '2025-06-24T00:00:00'
        }]
        df = clean_data(sample)
        self.assertEqual(df['Price'].dtype, 'float64')
        self.assertEqual(df['Rating'].dtype, 'float64')
        self.assertTrue('int' in str(df['Colors'].dtype))

if __name__ == '__main__':
    unittest.main()
