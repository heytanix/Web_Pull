import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url, components):
    # Send a GET request to the URL
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve content from {url}")
        return None

    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize a dictionary to hold the scraped data
    data = {component: [] for component in components}

    # Scrape the selected components
    if "title" in components:
        title = soup.title.string if soup.title else "No title found"
        data["title"].append(title)

    if "paragraph" in components:
        paragraphs = soup.find_all('p')
        for para in paragraphs:
            data["paragraph"].append(para.get_text())

    if "header" in components:
        headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        for header in headers:
            data["header"].append(header.get_text())

    return data

def main():
    print("Welcome to the Web Scraping Tool.")
    
    # Get URL from user
    url = input("Enter the URL of the website to scrape: ")
    
    # Ask the user for components to scrape
    print("Which components would you like to scrape? (select multiple by comma):")
    print("1. title")
    print("2. paragraph")
    print("3. header")
    print("4. all")
    
    user_input = input("Enter your choice (e.g., title, paragraph, header, all): ").strip().lower()
    
    # Determine which components to scrape
    if user_input == 'all':
        components_to_scrape = ["title", "paragraph", "header"]
    else:
        components_to_scrape = [comp.strip() for comp in user_input.split(",") if comp.strip() in ["title", "paragraph", "header"]]

    # Scrape the website
    scraped_data = scrape_website(url, components_to_scrape)

    if scraped_data:
        # Convert to DataFrame for easy viewing and manipulation
        df = pd.DataFrame(dict([(k, pd.Series(v)) for k,v in scraped_data.items()]))
        print("\nScraped Data:")
        print(df)

# Run the program
if __name__ == "__main__":
    main()
