import requests
from bs4 import BeautifulSoup
import json
import random

base_url = 'https://www.ralphlauren.com/men-clothing-polo-shirts'
products_list = []
max_pages = 4 

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15A372 Safari/604.1'
]

headers = {
    'User-Agent': random.choice(user_agents),
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

response = requests.get(base_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = soup.find_all('div', class_='product-data-info') 

    if not products:
        print("No products found.")
    else:
        for product in products:
            name_tag = product.find('a', class_='name-link js-pdp-link')
            price_tag = product.find('span', class_='lowcblack')
            lowered_price_tag = product.find('span', class_='lowred') 
            image_tag = product.find('img', class_='swiper-lazy swiper-lazy-loaded')
            image_url = image_tag['src'] if image_tag else 'N/A'  

            name = name_tag.text.strip() if name_tag else 'N/A'
            price = price_tag.text.strip() if price_tag else 'N/A'
            lowered_price = lowered_price_tag.text.strip() if lowered_price_tag else None     

            product_info = {
                'name': name,
                'price': price,
                'lowered_price': lowered_price,  
                'is_lowered': lowered_price is not None,  
                'image_url': image_url, 
            }

            products_list.append(product_info)

        with open('ralphlauren_polos.json', 'w') as json_file:
            json.dump(products_list, json_file, indent=4)

        print("Data saved to ralphlauren_polos.json")
else:
    print(f"Failed to retrieve page, Status Code: {response.status_code}")
