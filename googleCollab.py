from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://colab.research.google.com/")

    time.sleep(5)

    sign_in_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Sign in'))
        )
    sign_in_link.click()

    driver.switch_to.window(driver.window_handles[-1])

    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="email"]'))
    )
    email_input.send_keys('abc@gmail.com')

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#identifierNext button'))
    )
    next_button.click()

    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]'))
    )
    password_input.send_keys('')

    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#passwordNext button'))
    )
    sign_in_button.click()

except:
    pass
