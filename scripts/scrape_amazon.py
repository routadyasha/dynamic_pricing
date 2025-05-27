import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from fake_useragent import UserAgent

def get_html(url):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    response = requests.get(url, headers=headers)
    if response.status_code ==200:
        return response.text
    else:
        print("Failed to fetch page:", response.status_code)
        return None
    
def parse_amazon_search_result(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select(".s-result-item[data-component-type='s-search-result']")

    products = []
    for item in items:
        title = item.h2.text.strip() if item.h2 else None
        
        url = None
        if item.h2 and item.h2.a:
            url = "https://www.amazon.in" + item.h2.a['href']

        price_elem = item.select_one(".a-price-whole")
        price = price_elem.text.replace(",", "") if price_elem else None
        
        rating_elem = item.select_one(".a-icon-alt")
        rating = rating_elem.text.split()[0] if rating_elem else None
        
        reviews_elem = item.select_one(".a-size-base.s-underline-text")
        reviews = reviews_elem.text.replace(",", "") if reviews_elem else None

        if title and price:
            products.append({
                "title": title,
                "price": price,
                "rating": rating,
                "reviews": reviews,
                "url": url
            })

    return products

def scrape_amazon_smartphone(num_pages=1):
    all_products = []
    for page in range(1, num_pages+1):
        search_url = f"https://www.amazon.in/s?k=smartphones&page={page}"
        html = get_html(search_url)
        if html:
            products = parse_amazon_search_result(html)
            all_products.extend(products)
            print(f"Scraped page {page}, found {len(products)} products")
        time.sleep(3)

    df = pd.DataFrame(all_products)
    df.to_csv("data/raw/amazon_smartphones.csv", index=False)
    print("Saved scraped data to data/raw/amazon_smartphones.csv")

if __name__ == "__main__":
    scrape_amazon_smartphone(num_pages=3)