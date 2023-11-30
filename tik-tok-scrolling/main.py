import time
import undetected_chromedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = undetected_chromedriver.Chrome()

try:
    driver.get('https://www.tiktok.com/?lang=ru-RU')
    time.sleep(555)

    click_recommendation = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-1dhhdo4-SpanMainNavText"))
    )

    click_recommendation.click()
    time.sleep(1)

    svg_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "css-1anes8e-StyledIcon"))
    )

    svg_element.click()
    time.sleep(1)

    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(2)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()