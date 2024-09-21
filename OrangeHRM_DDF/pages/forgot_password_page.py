from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):  # Class for Forgot Password Page
    # Mention the locators
    FORGOT_PASSWORD = (By.XPATH, "//p[text()='Forgot your password? ']")
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    RESET_BUTTON = (By.XPATH, "//button[text()=' Reset Password ']")

    def forgot_password(self, username):  # Method to login
        self.click_element(self.FORGOT_PASSWORD)
        self.enter_text(self.USERNAME, username)
        self.click_element(self.RESET_BUTTON)
