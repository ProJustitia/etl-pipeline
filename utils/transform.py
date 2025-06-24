import pandas as pd

def clean_data(data):
    df = pd.DataFrame(data)

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df = df[~df['Title'].str.contains("Unknown Product")]
    df = df[~df['Title'].str.endswith(".jpeg")]

    df['Price'] = df['Price'].str.replace("$", "").astype(float) * 16000
    df['Rating'] = df['Rating'].str.extract(r'(\d+\.?\d*)').astype(float)
    df['Colors'] = df['Colors'].str.extract(r'(\d+)').astype(int)
    df['Size'] = df['Size'].str.replace("Size: ", "")
    df['Gender'] = df['Gender'].str.replace("Gender: ", "")

    return df
