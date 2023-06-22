# Amazon-Product-Scraper
This project is a web scraper implemented in Python that extracts product information from Amazon. It retrieves details such as product links, names, prices, ratings, and reviews for a given search query (in this case, "bags") and stores the data in a CSV file. Additionally, it scrapes additional information for each product, including descriptions, ASIN (Amazon Standard Identification Number), and manufacturer details.

## Dependencies
To run this project, you need to have the following dependencies installed:
- requests
- BeautifulSoup
- pandas

## Data Description
The scraped data includes the following fields:

- Product URL: The URL of the product on Amazon.
- Product Name: The name or title of the product.
- Product Price: The price of the product.
- Product Rating: The rating of the product, if available.
- Number of Reviews: The number of reviews the product has received.
- Product Description: The description of the product, if available.
- ASIN: The Amazon Standard Identification Number of the product, if available.
- Manufacturer: The manufacturer or brand of the product, if available.

## Limitations and Future Enhancements
This code scrapes a limited number of products (up to 200). You can modify the range in the loop to increase the number of products scraped.
The code assumes the HTML structure of the Amazon website remains the same. If Amazon updates its website structure, the code may need modifications.
Error handling for missing elements or unexpected HTML structure could be improved to make the scraper more robust.

## Acknowledgments
The project utilizes the requests library to make HTTP requests to the Amazon website.
The project uses the BeautifulSoup library for parsing HTML content.
The scraped data is stored and manipulated using the pandas library.
