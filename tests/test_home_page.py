from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import BASE_URL

def test_home_page_content(driver):
    driver.get(BASE_URL)
    try:
        header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        assert header.text == "Zwierzaki", "Incorrect content"
    finally:
        driver.quit()


