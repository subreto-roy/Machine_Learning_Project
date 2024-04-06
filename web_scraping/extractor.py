# import requests
# from bs4 import BeautifulSoup

# def extract_data(url, schema):
#     response = requests.get(url)
#     response.raise_for_status()  
    
#     #
#     soup = BeautifulSoup(response.content, 'html.parser')
    
    
#     extracted_data = {}
    
    
#     for item in schema:
#         if item.lower() == 'name':
#             extracted_data['name'] = soup.find('h1', {'id': 'title'}).get_text(strip=True)
#         elif item.lower() == 'author':
#             extracted_data['author'] = soup.find('span', {'class': 'author'}).get_text(strip=True)
#         elif item.lower() == 'format':
           
#             extracted_data['format'] = []
#             format_sections = soup.find_all('div', {'class': 'format-section'})
#             for section in format_sections:
#                 format_type = section.find('span', {'class': 'format-type'}).get_text(strip=True)
#                 price = section.find('span', {'class': 'price'}).get_text(strip=True)
#                 availability = section.find('span', {'class': 'availability'}).get_text(strip=True)
#                 extracted_data['format'].append({'type': format_type, 'price': price, 'availability': availability})

#     return extracted_data

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
