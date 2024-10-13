import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url, components):
    """
    Scrapes specified components from the given URL.

    Args:
        url (str): The URL of the website to scrape.
        components (list): The list of components to scrape.

    Returns:
        dict: A dictionary containing the scraped data.
    """
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to load the page. Status code: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    scraped_data = {}

    if 'title' in components:
        title = soup.title.string if soup.title else 'No title found'
        scraped_data['title'] = title

    if 'paragraphs' in components:
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        scraped_data['paragraphs'] = paragraphs

    if 'links' in components:
        links = [a['href'] for a in soup.find_all('a', href=True)]
        scraped_data['links'] = links

    return scraped_data

def save_to_csv(data, filename):
    """
    Saves the scraped data to a CSV file.

    Args:
        data (dict): The data to save.
        filename (str): The filename for the CSV file.
    """
    # Create a DataFrame from the data
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    print("Welcome to the Web Scraping Tool!")
    url = input("Enter the URL of the website to scrape: ")

    print("Select the components you want to scrape:")
    print("1. Title")
    print("2. Paragraphs")
    print("3. Links")
    print("4. All")

    choice = input("Enter your choice (1/2/3/4): ")

    components = []
    if choice == '1':
        components.append('title')
    elif choice == '2':
        components.append('paragraphs')
    elif choice == '3':
        components.append('links')
    elif choice == '4':
        components = ['title', 'paragraphs', 'links']
    else:
        print("Invalid choice. Please select again.")
        return

    # Scrape the website
    try:
        scraped_data = scrape_website(url, components)
        print("\nScraped Data:")
        for component, content in scraped_data.items():
            print(f"{component.capitalize()}: {content if isinstance(content, str) else len(content)} items found.")

        # Save to CSV
        filename = input("Enter the filename to save the data (e.g., scraped_data.csv): ")
        save_to_csv(scraped_data, filename)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
