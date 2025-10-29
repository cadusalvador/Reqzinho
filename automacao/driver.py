import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from utils.helpers import log

def start_driver_window(driver_path, binary_location):
    service = ChromeService(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    options.add_argument(f'--window-size=1920,1080')

    options.binary_location = binary_location
    driver = webdriver.Chrome(service=service, options=options)

    return driver