# Selenium Chrome Login Test (No webdriver-manager required)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import socket


# Function to check internet connection
def check_internet():
    try:
        socket.create_connection(("google.com", 80), timeout=5)
        return True
    except:
        return False


def test_website_login(username, password):

    driver = None

    # Check internet
    if not check_internet():
        print("No Internet Connection")
        return

    print("Internet Connected")

    try:
        # Start Chrome browser
        driver = webdriver.Chrome()

        wait = WebDriverWait(driver, 15)

        # Open Google login page
        driver.get("https://accounts.google.com/")

        # Enter email
        email_box = wait.until(
            EC.presence_of_element_located((By.ID, "identifierId"))
        )
        email_box.send_keys(username)
        email_box.send_keys(Keys.RETURN)

        # Enter password
        password_box = wait.until(
            EC.presence_of_element_located((By.NAME, "Passwd"))
        )
        password_box.send_keys(password)
        password_box.send_keys(Keys.RETURN)

        try:
            # Detect login success
            wait.until(EC.url_contains("myaccount.google.com"))
            print("VALID LOGIN")

        except TimeoutException:
            print("INVALID EMAIL OR PASSWORD")

    except Exception as e:
        print("Error occurred:", e)

    finally:
        if driver:
            driver.quit()


# Take user input
email = input("Enter Email: ")
password = input("Enter Password: ")

# Run the login test
test_website_login(email, password)


# Take input from user
email = input("Enter Email: ")
password = input("Enter Password: ")

# Run test
test_website_login(email, password)
