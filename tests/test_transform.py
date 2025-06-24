from utils.transform import clean_data

def test_transform_types():
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
    assert df['Price'].dtype == 'float64'
    assert df['Rating'].dtype == 'float64'
    assert df['Colors'].dtype == 'int32' or 'int64'