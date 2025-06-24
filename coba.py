import requests
from bs4 import BeautifulSoup

url = "https://fashion-studio.dicoding.dev/?page=1"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

collection = soup.select_one("#collectionlist")
print(collection.prettify()[:1000])  # tampilkan isi 1000 karakter pertama
