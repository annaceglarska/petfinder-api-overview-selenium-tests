from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def create_driver(browser="chrome", headless=False):

    browser = browser.lower()

    if browser == "chrome":
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )

    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")
        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )

    elif browser == "edge":
        edge_options = EdgeOptions()
        if headless:
            edge_options.add_argument("--headless")
            edge_options.add_argument("--disable-gpu")
        return webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=edge_options
        )

    else:
        raise ValueError(f"Unsupported browser: {browser}. Choose 'chrome', 'firefox' or 'edge'.")

def quit_driver(driver):

    if driver:
        driver.quit()
