import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import threading
import http.server
import socketserver
import time

# The Docker container runs on port 8888
PORT = 8888

# Removed local HTTP server fixture since we are testing the Docker container

@pytest.fixture
def browser():
    """
    Setup and teardown for Selenium WebDriver.
    This fixture runs before each test and provides a fresh browser instance.
    """
    # --- Setup ---
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    # Allow local file access for CORS
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--allow-file-access-from-files')
    
    # Initialize Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)  # Wait up to 10s for elements to appear
    driver.maximize_window()
    
    # Open via HTTP server
    driver.get(f'http://localhost:{PORT}/index.html')
    
    yield driver  # This is where the test runs
    
    # --- Teardown ---
    driver.quit()  # Close the browser after the test is done


@pytest.fixture
def home_browser():
    """
    Setup for testing the home page.
    """
    chrome_options = Options()

    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--allow-file-access-from-files')
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(f'http://localhost:{PORT}/home.html')
    
    yield driver
    
    driver.quit()


@pytest.fixture
def food_browser():
    """
    Setup for testing the food places page.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--allow-file-access-from-files')
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(f'http://localhost:{PORT}/food-places.html')
    
    yield driver
    
    driver.quit()
