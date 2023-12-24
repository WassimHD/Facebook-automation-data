from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import json

def initiliaze_driver():
    try:
        #driver_path="/Users/macbookpro/Desktop/scraping app/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--lang=en-us")
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e :
        print(f" error occured during initalizing driver : {str(e)}")

def facebook_login(driver):
    try:
        with open('Fastapi/config.json') as f:
            config = json.load(f)
            email=config.get('credentiels').get('email')
            password=config.get('credentiels').get('password')
            xpaths=config.get('xpaths')
    except FileNotFoundError as e:
        print(f"Error: {e}. File 'config.json' not found.")
    try:
        print('logging to facebook ...')
        driver.get("https://www.facebook.com/")
        time.sleep(7)
        email_field=driver.find_element(By.XPATH,xpaths['email_field'])
        email_field.send_keys(email)
        password_field=driver.find_element(By.XPATH,xpaths['password_field'])
        password_field.send_keys(password)
        login_btn=driver.find_element(By.XPATH,xpaths['login_btn'])
        login_btn.click()
        time.sleep(15)
        print("quitting driver")
        return driver
    except Exception as e :
        print(f" error occured : {str(e)}")


