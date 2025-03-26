

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes():
    # Target website
    url = "http://quotes.toscrape.com"
    
    try:
        # Get webpage content
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all quote containers
        quotes = []
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            
            quotes.append({
                'quote': text,
                'author': author,
                'tags': tags
            })
        
        # Convert to DataFrame
        df = pd.DataFrame(quotes)
        
        # Save to CSV
        df.to_csv('quotes.csv', index=False)
        print(f"Successfully scraped {len(quotes)} quotes")
        return df
        
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    quotes_data = scrape_quotes()
    print("\nFirst few quotes:")
    print(quotes_data.head())
