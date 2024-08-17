from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import sys
import logging

# Configure logging
logging.basicConfig(filename='search_script.log', level=logging.INFO)

def search_google(query):
    logging.info(f'Searching Google for: {query}')
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get(f"https://www.google.com/search?q={query}")
    
    search_results = driver.find_elements('css selector', 'h3')
    for result in search_results:
        print(result.text)
    
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_google(' '.join(sys.argv[1:]))
    else:
        print("Usage: python search_edge.py <search_query>")
