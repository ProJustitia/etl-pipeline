import pandas as pd

def clean_data(data):
    df = pd.DataFrame(data)

    # Remove nulls and invalids
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df = df[~df['Title'].str.contains("Unknown Product")]
    df = df[~df['Title'].str.endswith(".jpeg")]

    # Transform price
    df['Price'] = df['Price'].str.replace("$", "").astype(float) * 16000

    # Clean rating
    df['Rating'] = df['Rating'].str.extract(r'(\d+\.?\d*)').astype(float)

    # Clean colors
    df['Colors'] = df['Colors'].str.extract(r'(\d+)').astype(int)

    # Clean size
    df['Size'] = df['Size'].str.replace("Size: ", "")

    # Clean gender
    df['Gender'] = df['Gender'].str.replace("Gender: ", "")

    return df
