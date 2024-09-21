from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):  # Method to find the element
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_element_clickable(self, locator, timeout=10):  # Method to find the clickable element
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator, timeout=10):  # Method to click the element
        element = self.find_element_clickable(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=10):  # Method to send keys to the element
        element = self.find_element(locator, timeout)
        element.send_keys(text)

    def get_current_url(self):  # Method to get the current url
        return self.driver.current_url
