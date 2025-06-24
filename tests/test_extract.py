from utils.extract import extract_data

def test_extract_not_empty():
    data = extract_data()
    assert len(data) > 0
    assert all('Title' in item for item in data)