# Web Scraping Tool - Web Pull

This project is a simple Python-based web scraping tool that allows users to scrape specific components from a website and save the extracted data to a CSV file.

## Features
- Scrapes the following components from a webpage:
  - **Title**: The title of the webpage.
  - **Paragraphs**: All paragraph text (`<p>` tags).
  - **Headers**: Headers from `<h1>` to `<h6>`.
- Allows users to choose specific components to scrape or scrape all available components.
- Saves the scraped data into a CSV file.

## Requirements
- **Python 3.x**
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`

Install the required libraries using pip:
```bash
pip install requests beautifulsoup4 pandas
