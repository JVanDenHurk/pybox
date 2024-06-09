import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def init_driver(chrome_driver_path):
    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Optional: Run Chrome in headless mode

    # Initialize the ChromeDriver service
    service = Service(chrome_driver_path)

    # Start the WebDriver with the configured options and service
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_page(driver, url):
    try:
        # Navigate to the URL
        driver.get(url)

        # Wait for the page to load (adjust the sleep time as needed)
        time.sleep(1)

        # Use BeautifulSoup to parse the page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find the markdown element
        markdown_element = soup.find("markdown")

        if markdown_element:
            # Extract all content within the markdown tags, including the tags themselves
            markdown_content = markdown_element.prettify()
            return markdown_content
        else:
            print("Markdown element not found.\n")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

# Path to your ChromeDriver executable
chrome_driver_path = 'C:/Users/justi/Desktop/scrape/chromedriver-win64/chromedriver.exe'  # Change this to your ChromeDriver path

# Initialize the WebDriver
driver = init_driver(chrome_driver_path)

# Create an empty dictionary to store scraped data
scraped_data = {}

# URLs of pages 1 to 5 to scrape for testing
base_url = "https://etherfields-secret-scripts.web.app/core/"
for page_number in range(1, 1233):
    url = f"{base_url}{page_number}"
    print(f"Scraping page {page_number}...\n")
    markdown_content = scrape_page(driver, url)
    if markdown_content:
        print(f"Scraping of page {page_number} complete.\n")
        # Add scraped content to the dictionary with script number as key
        scraped_data[str(page_number)] = {"text": markdown_content}

# Close the WebDriver after scraping all pages
driver.quit()

# Save the scraped data to a JSON file
json_file_path = "secret_scripts.json"
with open(json_file_path, "w") as json_file:
    json.dump(scraped_data, json_file, indent=4)

print("Scraped data saved to:", json_file_path)