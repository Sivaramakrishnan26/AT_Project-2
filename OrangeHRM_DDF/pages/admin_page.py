from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class AdminPage(BasePage):  # Class for Admin Page
    # Locators of Header
    USER_MANAGEMENT = (By.XPATH, "//span[text()='User Management ']")
    JOB = (By.XPATH, "//span[text()='Job ']")
    ORGANIZATION = (By.XPATH, "//span[text()='Organization ']")
    QUALIFICATIONS = (By.XPATH, "//span[text()='Qualifications ']")
    NATIONALITIES = (By.XPATH, "//a[text()='Nationalities']")
    CORPORATE_BRANDING = (By.XPATH, "//a[text()='Corporate Branding']")
    CONFIGURATION = (By.XPATH, "//span[text()='Configuration ']")

    # Locators of Menu
    ADMIN = (By.XPATH, "//span[text()='Admin']")
    PIM = (By.XPATH, "//span[text()='PIM']")
    LEAVE = (By.XPATH, "//span[text()='Leave']")
    TIME = (By.XPATH, "//span[text()='Time']")
    RECRUITMENT = (By.XPATH, "//span[text()='Recruitment']")
    MY_INFO = (By.XPATH, "//span[text()='My Info']")
    PERFORMANCE = (By.XPATH, "//span[text()='Performance']")
    DASHBOARD = (By.XPATH, "//span[text()='Dashboard']")
    MAINTENANCE = (By.XPATH, "//span[text()='Maintenance']")
    CLAIM = (By.XPATH, "//span[text()='Claim']")
    BUZZ = (By.XPATH, "//span[text()='Buzz']")

    # Method to validate Header on Admin Page
    def title(self):
        self.click_element(self.ADMIN)
        time.sleep(5)

        user_management = self.find_element(self.USER_MANAGEMENT)
        if user_management:  # in self.driver.page_source:
            print("USER MANAGEMENT is present in the Header of Admin Page")
        else:
            print("USER MANAGEMENT is not present in the Header of Admin Page")

        job = self.find_element(self.JOB)
        if job:  # in self.driver.page_source:
            print("JOB is present in the Header of Admin Page")
        else:
            print("JOB is not present in the Header of Admin Page")

        organization = self.find_element(self.ORGANIZATION)
        if organization:  # in self.driver.page_source:
            print("ORGANIZATION is present in the Header of Admin Page")
        else:
            print("ORGANIZATION is not present in the Header of Admin Page")

        qualifications = self.find_element(self.QUALIFICATIONS)
        if qualifications:  # in self.driver.page_source:
            print("QUALIFICATIONS is present in the Header of Admin Page")
        else:
            print("QUALIFICATIONS is not present in the Header of Admin Page")

        nationalities = self.find_element(self.NATIONALITIES)
        if nationalities:  # in self.driver.page_source:
            print("NATIONALITIES is present in the Header of Admin Page")
        else:
            print("NATIONALITIES is not present in the Header of Admin Page")

        corporate_branding = self.find_element(self.CORPORATE_BRANDING)
        if corporate_branding:  # in self.driver.page_source:
            print("CORPORATE_BRANDING is present in the Header of Admin Page")
        else:
            print("CORPORATE_BRANDING is not present in the Header of Admin Page")

        configuration = self.find_element(self.CONFIGURATION)
        if configuration:  # in self.driver.page_source:
            print("CONFIGURATION is present in the Header of Admin Page")
        else:
            print("CONFIGURATION is not present in the Header of Admin Page")

    # Method to validate Menu on Admin Page
    def menu(self):
        admin = self.find_element(self.ADMIN)
        if admin:  # in self.driver.page_source:
            print("ADMIN is present in the Menu of Admin Page")
        else:
            print("ADMIN is not present in the Menu of Admin Page")

        pim = self.find_element(self.PIM)
        if pim:  # in self.driver.page_source:
            print("PIM is present in the Menu of Admin Page")
        else:
            print("PIM is not present in the Menu of Admin Page")

        leave = self.find_element(self.LEAVE)
        if leave:  # in self.driver.page_source:
            print("LEAVE is present in the Menu of Admin Page")
        else:
            print("LEAVE is not present in the Menu of Admin Page")

        times = self.find_element(self.TIME)
        if times:  # in self.driver.page_source:
            print("TIME is present in the Menu of Admin Page")
        else:
            print("TIME is not present in the Menu of Admin Page")

        recruitment = self.find_element(self.RECRUITMENT)
        if recruitment:  # in self.driver.page_source:
            print("RECRUITMENT is present in the Menu of Admin Page")
        else:
            print("RECRUITMENT is not present in the Menu of Admin Page")

        my_info = self.find_element(self.MY_INFO)
        if my_info:  # in self.driver.page_source:
            print("MY INFO is present in the Menu of Admin Page")
        else:
            print("MY INFO is not present in the Menu of Admin Page")

        performance = self.find_element(self.PERFORMANCE)
        if performance:  # in self.driver.page_source:
            print("PERFORMANCE is present in the Menu of Admin Page")
        else:
            print("PERFORMANCE is not present in the Menu of Admin Page")

        dashboard = self.find_element(self.DASHBOARD)
        if dashboard:  # in self.driver.page_source:
            print("DASHBOARD is present in the Menu of Admin Page")
        else:
            print("DASHBOARD is not present in the Menu of Admin Page")

        maintenance = self.find_element(self.MAINTENANCE)
        if maintenance:  # in self.driver.page_source:
            print("MAINTENANCE is present in the Menu of Admin Page")
        else:
            print("MAINTENANCE is not present in the Menu of Admin Page")

        claim = self.find_element(self.CLAIM)
        if claim:  # in self.driver.page_source:
            print("CLAIM is present in the Menu of Admin Page")
        else:
            print("CLAIM is not present in the Menu of Admin Page")

        buzz = self.find_element(self.BUZZ)
        if buzz:  # in self.driver.page_source:
            print("BUZZ is present in the Menu of Admin Page")
        else:
            print("BUZZ is not present in the Menu of Admin Page")
