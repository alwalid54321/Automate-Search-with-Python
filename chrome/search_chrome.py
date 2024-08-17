from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys
import logging

# Configure logging
logging.basicConfig(filename='search_script.log', level=logging.INFO)

def search_google(query):
    logging.info(f'Searching Google for: {query}')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"https://www.google.com/search?q={query}")
    
    search_results = driver.find_elements('css selector', 'h3')
    for result in search_results:
        print(result.text)
    
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_google(' '.join(sys.argv[1:]))
    else:
        print("Usage: python search_chrome.py <search_query>")
