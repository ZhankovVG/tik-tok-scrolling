import time
import undetected_chromedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decouple import config
from selenium.common.exceptions import NoSuchElementException


driver = undetected_chromedriver.Chrome()

try:
    driver.get('https://www.tiktok.com/?lang=ru-RU')
    time.sleep(3)

    # login button
    button_entry = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-e2e='top-login-button' and text()='Войти']"))
    )

    button_entry.click()
    time.sleep(3)

    # login name
    channel_item = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "css-1j4ihbo-DivBoxContainer"))
    )

    p_element = channel_item.find_element(
        By.XPATH, "//p[text()='Введите телефон / почту / имя пользователя']")

    p_element.click()
    time.sleep(3)

    # login link
    login_link = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Войти через эл. почту или имя пользователя"))
    )

    login_link.click()
    time.sleep(3)

    email = config("EMAIL")
    password = config("PASSWORD")

    # Username input
    username_input = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    username_input.send_keys(email)

    # Password input
    password_input = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "css-wv3bkt-InputContainer"))
    )

    password_input.send_keys(password)

    # Button entry
    login_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "e1w6iovg0"))
    )

    login_button.click()
    time.sleep(20)


# Pressing enter until it enters----------------------------


    def some_condition():
        try:
            driver.find_element(By.CLASS_NAME, "e1w6iovg0")
            return True
        except NoSuchElementException:
            return False

    while some_condition():
        login_button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "e1w6iovg0"))
        )

        # Click on the button
        login_button.click()
        time.sleep(10)
# ----------------------------------------------------------

    # Recommended videos
    click_recommendation = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "css-1dhhdo4-SpanMainNavText"))
    )

    click_recommendation.click()
    time.sleep(1)

    # Page scrolling
    for _ in range(5):
        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'span[data-e2e="like-icon"].css-6jur1x-SpanIconWrapper'))
        )

        like_button.click()

        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(10)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
