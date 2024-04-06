
import requests
from bs4 import BeautifulSoup

def extract_data(url, schema):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    extracted_data = {}
    
    for key, selector in schema.items():
        element = soup.select_one(selector)
        extracted_data[key] = element.get_text(strip=True) if element else 'Not found'

    return extracted_data
