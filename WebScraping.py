import requests
from bs4 import BeautifulSoup
import apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import json
import os

# Define the URL of the website to scrape
#url = "https://api.spotify.com/"

#url = "https://www.rokomari.com/book/"
url = "https://www.thedailystar.net/sports"


# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract news headlines (assuming headlines are in <h2> tags)

headlines = [headline.text for headline in soup.find_all("h2")]
print(headlines)

# Print the scraped headlines
for headline in headlines:
    print(headline)

news_url = "https://www.thedailystar.net/sports/"

news_url = "https://www.thedailystar.net/sports/"

data_file = os.path.join(os.getcwd(), "news_data.json")
print(data_file)

# Step 2.2: Implement web scraping logic


def scrape_news():
    try:
        # Send an HTTP GET request to the news website
        response = requests.get(news_url)
        print("hello kashim")
        response.raise_for_status()

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        print("hello kashim")

        # Extract relevant data (e.g., headlines) - modify as per your needs
        headlines = [headline.text.strip() for headline in soup.find_all("h2")]

        # Step 2.4: Store the scraped data in a structured format (JSON)
        data = {"headlines": headlines}

        # Determine the file path for storing JSON data
        data_file = os.path.join(os.getcwd(), "news_data.json")
        print(data_file)

        # Save the data to a JSON file
        with open(data_file, "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Scraped data successfully and saved to news_data.json")

    except Exception as e:
        print("Error:", e)


# Step 2.3: Schedule regular data scraping (e.g., daily at 9:00 AM)
scheduler = BlockingScheduler()
scheduler.add_job(scrape_news, "cron", hour=9)
scheduler.start()
# scrape_news()

# Define the URL of the website to scrape
#url = "https://www.cricketworldcup.com/"
url = "https://www.nytimes.com/international/"
# Send an HTTP GET request to the URL
response = requests.get(url)
print(response)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # SUB-MODULE 1: Extract News and Current Affairs Headlines
    news_headlines = []
    for headline in soup.find_all('div', class_='news-item'):
        title = headline.find('h3', class_='news-item__headline')
        author = headline.find('div', class_='news-item__author')
        if title and author:
            news_headlines.append({
                'title': title.text.strip(),
                'author': author.text.strip()
            })

    # SUB-MODULE 2: Extract Data from Integrated Affiliate Programs and Products
    affiliate_data = []
    for product in soup.find_all('div', class_='affiliate-product'):
        product_name = product.find('h3', class_='product-name')
        product_price = product.find('span', class_='product-price')
        if product_name and product_price:
            affiliate_data.append({
                'product_name': product_name.text.strip(),
                'product_price': product_price.text.strip()
            })

    # Print or process the extracted data
    print("SUB-MODULE 1: News Headlines")
    for news in news_headlines:
        print(f"Title: {news['title']}")
        print(f"Author: {news['author']}")
        print()

    print("SUB-MODULE 2: Affiliate Data")
    for product in affiliate_data:
        print(f"Product Name: {product['product_name']}")
        print(f"Product Price: {product['product_price']}")
        print()

else:
    print(
        f"Failed to retrieve the webpage. Status code: {response.status_code}")
