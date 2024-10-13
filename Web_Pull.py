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

def save_to_csv(data):
    # Convert to DataFrame for easy saving to CSV
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k,v in data.items()]))
    
    # Save DataFrame to a CSV file
    df.to_csv('scraped_data.csv', index=False)
    print("Data saved to 'scraped_data.csv'")

def main():
    print("Welcome to the Web Scraping Tool.")
    
    # Get URL from user
    url = input("Enter the URL of the website to scrape: ")
    
    # Ask the user for components to scrape
    print("Which components would you like to scrape? (select multiple by number):")
    print("1. Title")
    print("2. Paragraph")
    print("3. Header")
    print("4. All")
    
    user_input = input("Enter your choice (e.g., 1,2,3 or 4 for all): ").strip()
    
    # Determine which components to scrape
    if user_input == '4':
        components_to_scrape = ["title", "paragraph", "header"]
    else:
        component_options = {
            "1": "title",
            "2": "paragraph",
            "3": "header"
        }
        components_to_scrape = [component_options[num] for num in user_input.split(",") if num in component_options]
    
    # Scrape the website
    scraped_data = scrape_website(url, components_to_scrape)

    if scraped_data:
        print("\nScraped Data:")
        for key, value in scraped_data.items():
            print(f"{key.capitalize()}: {value}")

        # Save to CSV
        save_to_csv(scraped_data)

# Run the program
if __name__ == "__main__":
    main()
