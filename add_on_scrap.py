import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.remote_connection import LOGGER
import logging

# Set the log level for Marionette
LOGGER.setLevel(logging.WARNING)

options = webdriver.ChromeOptions()
time.sleep(3)
options.add_argument("--headless")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
browser = webdriver.Chrome(options=options)


try:
    # Connect to an existing Chrome browser session
    options = webdriver.ChromeOptions()
    options.debugger_address = "localhost:9222"
    browser = webdriver.Chrome(options=options)

    # Navigate to a webpage and print the page title
    time.sleep(3)
    browser.get("https://www.instagram.com")
    print(browser.title)


    # Find all the links that start with "cnd"
    time.sleep(2)

    # Loop through the links and print them out -- '//img[contains(@src, "cdninstagram.com/v")]'
    while True:
        img_elements = browser.find_elements(By.XPATH, '//img[contains(@src, "cdninstagram.com/v")]')
        for img in img_elements:
            src = img.get_attribute('src')
        if src and 'cnd' in src and '150x150' not in src:
            print(src)


except WebDriverException as e:
    print(f"An error occurred: {e}")


finally:
    # Close the browser
    input("Press enter to close the browser...")

