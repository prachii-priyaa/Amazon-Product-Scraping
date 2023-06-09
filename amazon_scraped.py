import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv

# Make a GET request to the URL
url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
response = requests.get(url)
response

product_links = []
product_names = []
product_prices = []
product_ratings = []
product_reviews = []

for page in range(1, 21):
    page_url = url + '&page=' + str(page)
    page_response = requests.get(page_url)
    page_content = BeautifulSoup(page_response.content, 'html.parser')
    products = page_content.find_all('div', {'class': 's-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border'})
    
    for product in products:
        # Get product link
        product_link = 'https://www.amazon.in' + product.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href']
        product_links.append(product_link)

        # Get product name
        product_name = product.find('h2', {'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).text.strip()
        product_names.append(product_name)

        # Get product price
        product_price = product.find('span', {'class': 'a-price-whole'}).text.strip()
        product_prices.append(product_price)

        # Get product rating
        product_rating = product.find('span', {'class': 'a-icon-alt'})
        product_ratings.append(product_rating)

        # Get number of product reviews
        product_review = product.find('span', {'class': 'a-size-base'}).text.strip().split()[0]
        product_reviews.append(product_review)

df_products = pd.DataFrame({
    'Product URL': product_links,
    'Product Name': product_names,
    'Product Price': product_prices,
    'Product Rating': product_ratings,
    'Number of Reviews': product_reviews
})


df_products

# Scrape additional information for each product
product_descriptions = []
product_asins = []
product_manufacturers = []

for product_links in df_products['Product URL'][:200]:
    product_response = requests.get(product_links)
    product_content = BeautifulSoup(product_response.content, 'html.parser')
    
    # Get product description
    try:
        product_description = product_content.find('div', {'id': "productDescription"}).text.strip()
    except AttributeError:
        product_description = ''
    product_descriptions.append(product_description)

    # Get product ASIN
    try:
        product_asin = product_content.find(soup.find('span', {'class': 'a-text-bold'})).text.strip()
        product_asins.append(product_asin)

    except AttributeError:
        product_asin = ''
    product_asins.append(product_asin)

    # Get product manufacturer
    try:
        product_manufacturer = product_content.find('a', {'id': 'bylineInfo'}).text.strip()
    except AttributeError:
        product_manufacturer = ''
    product_manufacturers.append(product_manufacturer)

df_additional_info = pd.DataFrame({
    'Product URL': df_products['Product URL'][:200],
    'Product Description': product_descriptions,
    'ASIN': product_asins,
    'Manufacturer': product_manufacturers
})


# Combine the two dataframes
df_combined = pd.merge(df_products, df_additional_info, on='Product URL', how='inner')

# Export the data to a CSV file
df_combined.to_csv('product_data.csv', index=False)

df_combined
