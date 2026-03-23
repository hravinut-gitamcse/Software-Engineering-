from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# The Selenium Manager automatically handles the driver for the chosen browser
driver = webdriver.Chrome()

try:
    # Navigate to Google.com
    driver.get("https://www.google.com")
    print(f"Navigating to {driver.current_url}")

    # Optional: Add an explicit wait to ensure the page is fully loaded and title is present
    WebDriverWait(driver, 10).until(EC.title_contains("Google"))
    
    # Get the actual page title
    actual_title = driver.title
    expected_title = "Google"

    # Check if the title matches the expected title
    if expected_title in actual_title:
        print(f"Verification is successful: Page title is '{actual_title}'")
    else:
        print(f"Verification failed: Expected title to contain '{expected_title}', but got '{actual_title}'")
    
finally:
    # Close the browser session
    driver.quit()
